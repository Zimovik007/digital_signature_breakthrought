from src.models import DocForGetSignature, DocForCheckSignature


def create_electronic_signature(doc: DocForGetSignature):
    return {
        "public_key": "1234567890",
        "signature": "123",
        "status": True
    }


def check_electronic_signature(doc: DocForCheckSignature):
    return {
        "status": "True"
    }
