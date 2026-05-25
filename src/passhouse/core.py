from __future__ import annotations

import base64
import json
import os
from typing import Any

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


def derive_key(password: str, salt: bytes) -> bytes:
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


def encrypt_vault(data: dict[str, Any], password: str, salt: bytes | None = None) -> bytes:
    salt = salt or os.urandom(16)
    token = Fernet(derive_key(password, salt)).encrypt(json.dumps(data, sort_keys=True).encode())
    return b"passhouse1:" + base64.urlsafe_b64encode(salt) + b":" + token


def decrypt_vault(blob: bytes, password: str) -> dict[str, Any]:
    try:
        marker, salt_raw, token = blob.split(b":", 2)
    except ValueError as exc:
        raise ValueError("invalid vault format") from exc
    if marker != b"passhouse1":
        raise ValueError("unsupported vault format")
    salt = base64.urlsafe_b64decode(salt_raw)
    try:
        clear = Fernet(derive_key(password, salt)).decrypt(token)
    except InvalidToken as exc:
        raise ValueError("wrong password or corrupt vault") from exc
    return json.loads(clear.decode())


def put_secret(vault: dict[str, Any], name: str, value: str) -> dict[str, Any]:
    next_vault = dict(vault)
    next_vault[name] = value
    return next_vault
