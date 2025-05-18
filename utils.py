import time
import random

def simulate_send_notification(n_type, message):
    # Simulate random failure
    success = random.choice([True, False])
    if not success:
        raise Exception("Simulated failure")
    print(f"{n_type} notification sent: {message}")
