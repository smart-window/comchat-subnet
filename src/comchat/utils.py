from typing import Literal, Any
import datetime
import requests
import base64
import re

def iso_timestamp_now() -> str:
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    iso_now = now.isoformat()
    return iso_now


def log(
    msg: str,
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: Any | None = None,
    flush: Literal[False] = False,
):
    print(
        f"[{iso_timestamp_now()}] " + msg,
        *values,
        sep=sep,
        end=end,
        file=file,
        flush=flush,
    )

# Get version from latest github
def get_version():
    url = "https://raw.githubusercontent.com/smart-window/comchat-subnet/main/src/comchat/__init__.py"
    response = requests.get(url, timeout=10)
    if not response.ok:
        print("Github api call failed!")
        return None

    content = response.json()['content']
    decoded_content = base64.b64decode(content).decode('utf-8')
    lines = decoded_content.split('\n')

    version_line = lines[0]
    version_match = re.search(r'__version__ = "(.*?)"', version_line)
    if not version_match:
        raise Exception("Version information not found!")

    return version_match.group(1)
