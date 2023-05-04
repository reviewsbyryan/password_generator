from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64


# Salt should be unique for each password, use metadata
def generate_password(master_password, salt):
    salt = salt.encode()  # Convert to bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(master_password.encode())  # Can only use kdf once
    password = base64.urlsafe_b64encode(key).decode()  # Convert to string and remove '=' padding
    return password.rstrip('=')


# Usage
master_password = input("master password: ")
salt = input("metadata: ")

password = generate_password(master_password, salt)
print(f'Password for {salt}: {password}')
