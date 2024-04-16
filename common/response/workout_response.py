import json
from enum import Enum

class Success(str, Enum):
    CREATED = "Created Successfully!"
    UPDATED = "Updated Successfully!"
    GET = "Fetched Successfully!"

class Error(str, Enum):
    INTERNAL_SERVER_ERROR = "Internal server error!"

class CustomResponse:
    def __init__(self, message, data=None, status=False, statusCode=None):
        self.message = message
        self.data = data
        self.status = status
        self.statusCode = statusCode

    def to_dict(self):
        return {
            "message": self.message,
            "data": self.data,
            "status": self.status,
            "statusCode": self.statusCode
        }

    def to_json(self):
        return json.dumps(self.to_dict())