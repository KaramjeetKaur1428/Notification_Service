import pika
import json
from models import SessionLocal, Notification
from utils import simulate_send_notification
import time

def process_notification(data, retries=3):
    db = SessionLocal()
    notif = db.query(Notification).filter(Notification.id == data['id']).first()

    for attempt in range(retries):
        try:
            simulate_send_notification(data["type"], data["message"])
            notif.status = "sent"
            db.commit()
            return
        except Exception as e:
            print(f"Retry {attempt+1} failed: {e}")
            time.sleep(1)

    notif.status = "failed"
    db.commit()

def callback(ch, method, properties, body):
    data = json.loads(body)
    process_notification(data)

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="notification_queue")
channel.basic_consume(queue="notification_queue", on_message_callback=callback, auto_ack=True)
print("Worker is running... Press CTRL+C to stop.")
channel.start_consuming()
