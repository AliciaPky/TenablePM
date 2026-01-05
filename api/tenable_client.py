from tenable.io import TenableIO
from config import TENABLE_ACCESS_KEY, TENABLE_SECRET_KEY

def get_tenable_client():
    if not TENABLE_ACCESS_KEY or not TENABLE_SECRET_KEY:
        raise Exception("Tenable API keys not found")

    return TenableIO(
        TENABLE_ACCESS_KEY,
        TENABLE_SECRET_KEY
    )
