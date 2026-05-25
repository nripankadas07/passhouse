import pytest
from passhouse.core import decrypt_vault, encrypt_vault, put_secret


def test_encrypt_roundtrip_and_wrong_password():
    vault = put_secret({}, "github", "token")
    blob = encrypt_vault(vault, "pw", salt=b"0" * 16)
    assert decrypt_vault(blob, "pw")["github"] == "token"
    with pytest.raises(ValueError):
        decrypt_vault(blob, "bad")
