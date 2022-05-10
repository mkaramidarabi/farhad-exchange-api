import dotenv
import hashlib
import hmac
import os

dotenv.load_dotenv()
secret = os.getenv("SECRET")


def query_string(content):
    signature = hmac.new(
        secret.encode("utf-8"), content.encode("utf-8"), hashlib.sha256
    ).hexdigest()
    print(signature)
    return signature
