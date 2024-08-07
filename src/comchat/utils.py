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

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the content of the file
        file_content = response.text
        lines = file_content.split('\n')

        version_line = lines[0]
        version_match = re.search(r'__version__ = "(.*?)"', version_line)
        if not version_match:
            raise Exception("Version information not found!")

        return version_match.group(1)
    else:
        print(f'Failed to retrieve file: {response.status_code}')
        return None
    