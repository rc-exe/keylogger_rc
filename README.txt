 Keylogger & Security Monitoring Tool

 Description
This is an ethical keylogger and security monitoring tool built using Python and Flask. It records keystrokes and captures screenshots at regular intervals. The data is stored in an SQLite database and displayed in a web-based UI for analysis.

 Features
- **Keystroke Logging:** Records all typed keys and stores them securely.
- **Automatic Screenshot Capture:** Takes screenshots at configurable time intervals.
- **Flask Web Dashboard:** View recorded keystrokes and screenshots in an easy-to-use interface.
- **User Authentication:** Login and logout functionality for secure access.
- **Database Storage:** Uses SQLite for storing key logs.
- **REST API:** Provides endpoints to fetch logs and screenshots.

 Installation
 Prerequisites
Ensure you have Python installed on your system. Then, install the required dependencies:
```bash
pip install flask pyautogui
```

 Running the Application
1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000/` in your browser.

 Configuration
- To change the **screenshot capture interval**, modify this line in `app.py`:
  ```python
  time.sleep(30)   Adjust time in seconds
  ```
- Change login credentials in `app.py`:
  ```python
  if username == 'admin' and password == 'password':
  ```
  Replace `'admin'` and `'password'` with your own credentials.

 API Endpoints
- `GET /api/logs` - Fetches recorded keystrokes.
- `GET /api/screenshots` - Lists captured screenshots.

 Caution ⚠️
 **Ethical Use Only**
This tool is designed for **ethical security monitoring** and **personal system analysis**. Unauthorized use for spying, hacking, or monitoring individuals without their consent **is illegal** and punishable under cybersecurity laws. Ensure you have proper authorization before deploying this tool.

 License
This project is intended for ethical use only. The author is **not responsible for any misuse** of this tool.

 Author
Ritesh Chakramani

 Contact
For queries, contact: **riteshchakramani123@gmail.com**

