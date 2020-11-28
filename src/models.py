from pydantic import BaseModel


class DocForGetSignature(BaseModel):
    text: str
    private_user_key: str


class DocForCheckSignature(BaseModel):
    text: str
    public_signature_key: str
    signature: str
