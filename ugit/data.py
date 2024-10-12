import hashlib
import os
from pathlib import Path

GIT_DIR = Path('.ugit')
OBJECTS_DIR = GIT_DIR / 'objects'


def init():
    os.makedirs(GIT_DIR)
    os.makedirs(OBJECTS_DIR)


def hash_object(data, type_='blob'):
    obj = type_.encode() + b'\x00' + data
    oid = hashlib.sha1(data).hexdigest()

    file = OBJECTS_DIR / oid
    file.write_bytes(obj)

    return oid


def get_object(oid, expected='blob'):
    file = OBJECTS_DIR / oid
    obj = file.read_bytes()

    type_, _, content = obj.partition(b'\x00')
    type_ = type_.decode()

    if expected is not None and type_ != expected:
        raise ValueError(f'Expected {expected}, got {type_}')

    return content
