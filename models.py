import uuid
from typing import Optional
# from fastapi.encoders import jsonable_encoder  # -- maybe useful, instead of selfmade ?field? "json_encoders"
from pydantic import BaseModel, Field

"""
class ObjId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: str):
        try:
            return cls(v)
        except:
            raise ValueError("Not a valid ObjectId")
"""

class Person(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    age: str = Field(...)
    gender: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "Don",
                "age": "15",
                "gender": "M"
            }
        }

"""
class Person(BaseModel):
    id: ObjId = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = None
    age: int = None
    gender: str = None

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "ObjectId('6411d24e8902d0564fca82a0')",
                "name": "Don",
                "age": "15",
                "gender": "M"
            }
        }
        json_encoders = {
            ObjId: lambda v: f"ObjectId('{str(v)}')",
        }
"""


class PersonUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    gender: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "Name": "Don",
                "age": "16",
                "gender": "M"
            }
        }