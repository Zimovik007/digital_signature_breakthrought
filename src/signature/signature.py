from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import os

from src.models import DocForGetSignature, DocForCheckSignature


def get_bytearray(text):
    b = bytearray()
    b.extend(map(ord, text))
    return b


def create_electronic_signature(doc: DocForGetSignature):
    input_bytes = doc.text if type(doc.text) == bytearray else get_bytearray(doc.text)
    key = RSA.generate(2048, os.urandom) if not len(doc.private_user_key) else doc.private_user_key
    h = SHA256.new(input_bytes)

    signature = pkcs1_15.new(key).sign(h)
    pubkey = key.publickey()

    return {
        "public_key": pubkey,
        "signature": signature,
        "status": True
    }


def check_electronic_signature(doc: DocForCheckSignature):
    status = False
    try:
        pkcs1_15.new(doc.public_signature_key).verify(SHA256.new(b'test'), doc.signature)
        status = True
    except ValueError:
        pass
    return {
        "status": status
    }
