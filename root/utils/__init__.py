import time
from os.path import join as join_path
from pathlib import Path

BASE_PATH = Path(__file__).parent.parent
UPLOAD_PATH = join_path(BASE_PATH, 'static')


def new_name(old_name: str):
    ext = old_name.split('.')[-1]
    return 'uploads/%s.%s' % (time.time_ns(), ext)
