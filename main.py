from fastapi import FastAPI
from src.models import DocForGetSignature, DocForCheckSignature
from src.signature import signature as sig

app = FastAPI()


@app.get("/")
def root():
    return {
        "event": "digital breakthrough",
        "team": "OkayBoomers"
    }


@app.post("/create_electronic_signature")
def create_electronic_signature(doc: DocForGetSignature):
    return sig.create_electronic_signature(doc)


@app.post("/check_electronic_signature")
def check_electronic_signature(doc: DocForCheckSignature):
    return sig.check_electronic_signature(doc)
