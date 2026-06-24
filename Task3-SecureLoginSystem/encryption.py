import os
import base64
import bcrypt
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# AES-256 Key (32 bytes)
key = base64.b64decode("MDEyMzQ1Njc4OWFiY2RlZjAxMjMONTY30DlhYmNKZWY=")

# Password Hashing
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

# Password Verification
def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())

# Encrypt Sensitive Data
def encrypt_data(text):
    aes = AESGCM(key)
    nonce = os.urandom(12)
    encrypted = aes.encrypt(nonce, text.encode(), None)
    return base64.b64encode(nonce + encrypted).decode()

# Decrypt Sensitive Data
def decrypt_data(cipher_text):
    data = base64.b64decode(cipher_text)
    nonce = data[:12]
    encrypted = data[12:]
    aes = AESGCM(key)
    return aes.decrypt(nonce, encrypted, None).decode()