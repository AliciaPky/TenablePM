import os
from dotenv import load_dotenv

load_dotenv()

TENABLE_ACCESS_KEY = os.getenv("TENABLE_ACCESS_KEY")
TENABLE_SECRET_KEY = os.getenv("TENABLE_SECRET_KEY")

JSON_OUTPUT_PATH = "data/tenable_health.json"
PDF_OUTPUT_PATH = "data/tenable_health_report.pdf"
