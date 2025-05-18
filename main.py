from fastapi import FastAPI, HTTPException
from schema import NotificationRequest, NotificationResponse
from models import Notification, SessionLocal, init_db
import pika
import json

app = FastAPI()
init_db()

@app.post("/notifications")
def send_notification(req: NotificationRequest):
    db = SessionLocal()
    notif = Notification(user_id=req.user_id, type=req.type, message=req.message)
    db.add(notif)
    db.commit()
    db.refresh(notif)

    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="notification_queue")

    channel.basic_publish(
        exchange='',
        routing_key='notification_queue',
        body=json.dumps({
            "id": notif.id,
            "user_id": req.user_id,
            "type": req.type,
            "message": req.message
        }),
    )
    connection.close()
    return {"message": "Notification queued."}

@app.get("/users/{user_id}/notifications", response_model=list[NotificationResponse])
def get_notifications(user_id: int):
    db = SessionLocal()
    return db.query(Notification).filter(Notification.user_id == user_id).all()
