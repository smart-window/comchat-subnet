import time
import argparse
import subprocess
from comchat.utils import get_version
from comchat import __version__ as current_version

def update_and_restart(pm2_name, key):
    global current_version
    subprocess.run(["pm2", "start", "src/comchat/cli.py", "--name", pm2_name, "--time", "--interpreter", "python3", "--", key])
    while True:
        latest_version = get_version()
        print(f"Current version: {current_version}")
        print(f"Latest version: {latest_version}")

        if current_version != latest_version and latest_version != None:
            print("Updating to the latest version...")
            subprocess.run(["pm2", "delete", pm2_name])
            subprocess.run(["git", "reset", "--hard"])
            subprocess.run(["git", "pull"])
            subprocess.run(["pip", "install", "-e", "."])
            subprocess.run(["pm2", "start", "cli.py", "--name", pm2_name, "--time", "--interpreter", "python3", "--", key])
            current_version = latest_version
        print("All up to date!")
        time.sleep(300)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Automatically update and restart the validator process when a new version is released.",
        epilog="ex: python3 start.py --pm2_name vali::comchat --key vali::comchat")

    parser.add_argument("--pm2_name", required=True, help="Name of the PM2 process.")
    parser.add_argument("--key", required=True, help="Name of the commune key.")

    args = parser.parse_args()

    try:
        update_and_restart(args.pm2_name, args.key)
    except Exception as e:
        parser.error(f"An error occurred: {e}")
