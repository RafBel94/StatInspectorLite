# StatInspectorLite

StatInspectorLite is a lightweight and efficient application developed in Python that allows you to monitor, log, and track the key statistics and status of your computer's components. This project is designed to help users stay informed about their system's performance and health in real-time.

---

## 🚀 Purpose

The primary purpose of StatInspectorLite is to provide an accessible and user-friendly tool that enables:

- **Monitoring** CPU and GPU usage and temperature.
- **Logging** RAM usage and the number of active processes on the system.
- **Alerting** the user if the CPU temperature exceeds 45 degrees, via notifications sent by a Telegram bot.
- **Storing** critical event logs in a MongoDB database for later analysis.

---

## 🛠️ Technologies Used

StatInspectorLite is built with the following technologies:

### Programming Language
- **Python**: The core of the project, used to handle monitoring logic, database management, and Telegram communication.

### Python Libraries
- **Psutil**: To retrieve information about CPU, GPU, RAM usage, and the number of active processes.
- **PyTelegramBotAPI**: To integrate the application with Telegram and send notifications to the user.
- **Pymongo**: To interact with a MongoDB database and store relevant logs.

### Database
- **MongoDB**: To store critical event logs, such as CPU temperatures exceeding the defined threshold.

### Notifications
- **Telegram Bot**: To send real-time alerts to the user when the CPU temperature exceeds 45 degrees Celsius.

---

## 📋 Key Features

1. **Real-time Monitoring:**
   - CPU usage.
   - CPU and GPU temperature.
   - RAM usage.
   - Number of active processes.

2. **Critical Event Logging:**
   - Events where the CPU temperature exceeds 45 degrees are automatically logged in a MongoDB database.

3. **Automated Notifications:**
   - Notifications sent to the user via Telegram in case of critical CPU temperature detection.

4. **Lightweight and Efficient:**
   - Designed to be non-intrusive and consume minimal system resources.

---

## 📦 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your_user/StatInspectorLite.git
   cd StatInspectorLite
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - **TELEGRAM_BOT_TOKEN**: The Telegram bot token.
   - **MONGO_URI**: The URI for connecting to the MongoDB database.

   You can configure these variables in a `.env` file.

5. Run the application:

   ```bash
   python main.py
   ```

---

## 🔧 Additional Configuration

- **Temperature Threshold:**
  - The temperature threshold for notifications is set to 45 degrees by default. You can modify it in the `config.py` file.

- **Telegram Bot:**
  - To get a token, create a bot on Telegram using [BotFather](https://core.telegram.org/bots#botfather).

---

## 🤝 Contributions

Contributions are welcome! If you wish to add new features, optimize performance, or fix bugs, feel free to open an issue or submit a pull request.

---

## 🛡️ License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## 📬 Contact

If you have any questions, issues, or suggestions, feel free to contact us:

- **Email:** your_email@example.com
- **Telegram:** [@your_user](https://t.me/your_user)

Thank you for using StatInspectorLite! 🎉
