from typing import Optional

from fastapi import FastAPI
from models import DocForGetSignature, DocForCheckSignature

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/create_electronic_signature")
def create_electronic_signature(doc: DocForGetSignature):
    return {"public_key": "1234567890", "status": "True"}


@app.post("/check_electronic_signature")
def check_electronic_signature(doc: DocForCheckSignature):
    return {"status": "True"}
