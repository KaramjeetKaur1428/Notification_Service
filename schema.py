from pydantic import BaseModel
from typing import List

class NotificationRequest(BaseModel):
    user_id: int
    type: str  # email, sms, in-app
    message: str

class NotificationResponse(BaseModel):
    id: int
    user_id: int
    type: str
    message: str
    status: str
