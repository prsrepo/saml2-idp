import os
from pathlib import Path

from flask_saml2.utils import certificate_from_file, private_key_from_file


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

KEY_DIR = os.path.join(BASE_DIR, "certificates", "keys")
CERTIFICATE_FILE = os.path.join(KEY_DIR, 'certificate.pem')
PRIVATE_KEY_FILE = os.path.join(KEY_DIR, 'private-key.pem')

CERTIFICATE = certificate_from_file(Path(CERTIFICATE_FILE))
PRIVATE_KEY = private_key_from_file(Path(PRIVATE_KEY_FILE))
