import json
import os
from datetime import date

DATA_DIR      = os.path.join(os.path.dirname(__file__), "..", "data")
PROFILES_FILE = os.path.join(DATA_DIR, "profiles.json")
LOGS_DIR      = os.path.join(DATA_DIR, "logs")


def _ensure_dirs():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(LOGS_DIR, exist_ok=True)


def load_profiles() -> list:
    _ensure_dirs()
    if not os.path.exists(PROFILES_FILE):
        return []
    with open(PROFILES_FILE, "r") as f:
        return json.load(f)


def save_profiles(profiles: list):
    _ensure_dirs()
    with open(PROFILES_FILE, "w") as f:
        json.dump(profiles, f, indent=2)


def _log_file(name: str) -> str:
    return os.path.join(LOGS_DIR, f"{name.lower()}_logs.json")


def load_logs(name: str) -> list:
    _ensure_dirs()
    path = _log_file(name)
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)


def save_log(name: str, entry: dict):
    _ensure_dirs()
    logs = load_logs(name)
    # Remove existing entry for same date if any
    logs = [l for l in logs if l.get("date") != entry.get("date")]
    logs.append(entry)
    with open(_log_file(name), "w") as f:
        json.dump(logs, f, indent=2)
