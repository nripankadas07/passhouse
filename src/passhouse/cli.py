from __future__ import annotations

import argparse
from pathlib import Path
from .core import decrypt_vault, encrypt_vault, put_secret


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Encrypted local secrets vault.")
    parser.add_argument("file")
    parser.add_argument("password")
    parser.add_argument("--put", nargs=2, metavar=("NAME", "VALUE"))
    args = parser.parse_args(argv)
    path = Path(args.file)
    vault = decrypt_vault(path.read_bytes(), args.password) if path.exists() else {}
    if args.put:
        vault = put_secret(vault, args.put[0], args.put[1])
        path.write_bytes(encrypt_vault(vault, args.password))
    else:
        print("\n".join(sorted(vault)))
    return 0
