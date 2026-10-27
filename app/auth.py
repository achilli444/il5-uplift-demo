import base64
import hashlib
import hmac
import json
import time

from . import settings


def hash_password(password: str) -> str:
    # G1: MD5 is not FIPS 140-validated and is unsuitable for password storage
    return hashlib.md5(password.encode()).hexdigest()


def issue_token(username: str) -> str:
    # G3: no expiry / idle timeout; token is valid forever
    payload = json.dumps({"sub": username, "iat": int(time.time())}).encode()
    sig = hmac.new(settings.TOKEN_SECRET.encode(), payload, hashlib.sha256).digest()
    return base64.urlsafe_b64encode(payload).decode() + "." + base64.urlsafe_b64encode(sig).decode()


def verify_token(token: str):
    try:
        p, s = token.split(".")
        payload = base64.urlsafe_b64decode(p)
        sig = base64.urlsafe_b64decode(s)
    except Exception:
        return None
    expected = hmac.new(settings.TOKEN_SECRET.encode(), payload, hashlib.sha256).digest()
    if not hmac.compare_digest(sig, expected):
        return None
    return json.loads(payload)
