from uuid import uuid4

from pydantic import BaseModel, Field

from .message import Message


class Conversation(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    user_message: Message | None = None
    messages: list[Message] = []
