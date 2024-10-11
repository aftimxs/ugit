import hashlib
import os
from pathlib import Path

GIT_DIR = Path('.ugit')
OBJECTS_DIR = GIT_DIR / 'objects'


def init():
    os.makedirs(GIT_DIR)
    os.makedirs(OBJECTS_DIR)


def hash_object(data):
    oid = hashlib.sha1(data).hexdigest()
    with open(OBJECTS_DIR / oid, 'wb') as f:
        f.write(data)
    return oid


def get_object(oid):
    with open(OBJECTS_DIR / oid, 'rb') as f:
        return f.read()
