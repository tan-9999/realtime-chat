# 💬 Realtime Chat Application

A basic real-time chat application built using **Django** and **ASGI** (Django Channels). This project demonstrates how to implement WebSockets in Django to enable instant messaging between users without page reloads.

## 🚀 Features

- **Real-time Messaging:** Instant message delivery using WebSockets.
- **Room Support:** Users can join specific chat rooms to talk to different groups.
- **User Authentication:** Integrated with Django's authentication system.
- **Message History:** (Optional) Messages persist in the database.
- **Responsive Design:** Basic UI compatible with desktop and mobile.

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Async Framework:** Django Channels (ASGI)
- **Message Broker:** Redis (via Docker or local installation)
- **Frontend:** HTML, CSS, JavaScript (Vanilla WebSocket API)
- **Database:** SQLite (default) / PostgreSQL

## 📋 Prerequisites

Before running the project, ensure you have the following installed:

- **Python** (3.8 or higher)
- **Redis** (Required for the Channel layer)

## ⚙️ Installation & Setup

Follow these steps to get the project running locally.

### 1. Clone the Repository
git clone https://github.com/tan-9999/realtime-chat.git
cd realtime-chat

text

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.
Windows
python -m venv venv
venv\Scripts\activate

macOS/Linux
python3 -m venv venv
source venv/bin/activate

text

### 3. Install Dependencies
pip install -r requirements.txt

text
> **Note:** If `requirements.txt` is missing, install the core packages manually:
> `pip install django channels channels-redis daphne`

### 4. Start Redis
Django Channels requires a Redis instance to handle message passing.
- **Using Docker (Recommended):**
docker run -p 6379:6379 -d redis:5

text
- **Or ensure your local Redis server is running.**

### 5. Apply Migrations
Set up the database tables.
python manage.py migrate

text

### 6. Run the Server
Start the ASGI development server.
python manage.py runserver

text

### 7. Access the App
Open your browser and navigate to:
`http://127.0.0.1:8000/`

---

## 📂 Project Structure

realtime-chat/

├── chat/ # Main chat application app

│ ├── consumers.py # WebSocket consumers (handles async events)

│ ├── routing.py # WebSocket URL routing

│ └── views.py # HTTP views

├── core/ # Project configuration

│ ├── asgi.py # ASGI entry point for the server

│ ├── settings.py # Django settings (includes Channels config)

│ └── urls.py # Main URL routing

├── templates/ # HTML templates

├── manage.py # Django command-line utility

└── requirements.txt # Project dependencies

text

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
💡 Quick Tips for Your Repo
Since your repo description mentions "Using Django with Asgi," ensure your settings.py is configured correctly for the channel layer. If you haven't added a requirements.txt file yet, run this command in your terminal to generate one before pushing:

bash
pip freeze > requirements.txt
