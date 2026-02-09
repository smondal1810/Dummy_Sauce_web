import os
from pathlib import Path

from dotenv import load_dotenv


env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(env_path)

BASE_URL = os.getenv("BASE_URL")
APP_USERNAME = os.getenv("APP_USERNAME")
APP_PASSWORD = os.getenv("APP_PASSWORD")
print("BASE_URL =", BASE_URL)
print("USERNAME =", APP_USERNAME)
print("PASSWORD =", APP_PASSWORD)

assert BASE_URL, "BASE_URL not loaded"
assert APP_USERNAME, "USERNAME not loaded"
assert APP_PASSWORD, "PASSWORD not loaded"
