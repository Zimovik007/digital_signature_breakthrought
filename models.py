from pydantic import BaseModel


class DocForGetSignature(BaseModel):
    text: str


class DocForCheckSignature(BaseModel):
    text: str
    key: str
