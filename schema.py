from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId
from typing import Optional


class MongoDBModel(BaseModel):
    id: Optional[ObjectId] = Field(alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class YourSchema(MongoDBModel):
    request_id: str
    author: str
    action: str
    from_branch: str
    to_branch: str
    timestamp: datetime
