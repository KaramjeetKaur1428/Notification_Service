# Notification_Service
PEPSALES INTERN ASSIGN. | System to send notifications to users.

# Notification Service
A scalable notification system built with **FastAPI** and **RabbitMQ** to send notifications via Email, SMS, and In-App messages with retry and queueing support.

--------------------------------------------------------------------------------------------------
## Features
- **API Endpoints**  
  📨 Send notifications (Email, SMS, In-App)
- 🐇 Queue-based processing using RabbitMQ
- 🔁 Retry logic for failed notifications
- 🗂️ SQLite for persistence (lightweight, no setup needed)
- 📱 REST API for sending and retrieving notifications

- **Notification Types**  
  Supports `email`, `sms`, and `in-app` notifications.

- **Queue & Retry Mechanism**  
  Uses RabbitMQ as a message queue for asynchronous processing with retries on failure.
---------------------------------------------------------------------------------------------------
## 🧰 Tech Stack
- Python 3.10+
- FastAPI
- SQLite (via SQLAlchemy)
- RabbitMQ
- Pika (RabbitMQ client)
- Uvicorn
----------------------------------------------------------------------------------------------------
## Project Structure
notificationapp/
├── main.py # FastAPI app entrypoint
├── requirements.txt # Python dependencies
├── app/
│ ├── init.py
│ ├── models.py     # (Pydantic models)
│ ├── routes.py     # (API routes)
│ ├── storage.py    # (In-memory data store)
│ ├── utils.py      # (Notification delivery logic)
│ └── consumer.py   # (RabbitMQ consumer (worker) )
└── producer.py     # (RabbitMQ producer for sending notifications to the queue)

-------------------------------------------------------------------------------------
## Setup & Run Instructions
### Prerequisites
              - Python 3.11+ installed  
              - Docker installed (for RabbitMQ)  
-------------------------------------------------------------------------------------
## 📦 Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/notification-service.git
cd notification-service

2.Install Dependencies
py -m pip install fastapi uvicorn sqlalchemy pika httpx

3. Start RabbitMQ
Make sure RabbitMQ is running locally on default settings (localhost:5672).
You can download RabbitMQ here.

4. Initialize the Database
py -c "from models import init_db; init_db()"

5. Start the FastAPI Server
py -m uvicorn main:app --reload

6. API will be live at: http://127.0.0.1:8000/docs
---------------------------------------------------------------------------------------------------
__API USAGE__
🔹 POST /notifications
Send a notification:

json
Copy code
{
  "user_id": "example@domain.com",
  "message": "Welcome to our service!",
  "type": "email"
}
Supported types: "email", "sms", "in-app"

🔹 GET /users/{user_id}/notifications
Retrieve all notifications for a user:

bash
Copy code
GET /users/example@domain.com/notifications
Response:

json
Copy code
[
  {
    "user_id": "example@domain.com",
    "message": "Welcome to our service!",
    "type": "email"
  }
]
-------------------------------------------------------------------------------------------
 How It Works
API receives notification → enqueues it to RabbitMQ.

Consumer picks message → tries to deliver it (with retry logic).

Successfully delivered notifications are stored in memory.
---------------------------------------------------------------------------------------------
📌 Example Scenario
Send an email to user@example.com via POST /notifications.

Worker receives from RabbitMQ → processes it.

User's notification is saved in memory.

Fetch it using GET /users/user@example.com/notifications.
-----------------------------------------------------------------------------------------------
📈 Potential Improvements
->Add persistent DB (PostgreSQL, MongoDB)
->Real email/SMS gateway integration (Twilio, SendGrid)
->User authentication system
->dmin dashboard for managing notifications
------------------------------------------------------------------------------------------------
🙋‍♀️ Author
Karamjeet Kaur
📧 22051428@kiit.ac.in
🌐 LinkedIn : https://www.linkedin.com/in/karamjeet-kaur-717a43217/
