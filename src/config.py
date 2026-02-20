from pathlib import Path
import os

# ---------------------------------
# Project root

BASE_DIR = Path(__file__).resolve().parents[2]

# Data path 

DATA_DIR  = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

RAW_WEATHER_FILE = RAW_DATA_DIR / "api_data.json"
CLEANED_EXCHANGE_RATE_FILE = PROCESSED_DATA_DIR / "cleaned_data.csv"

# --------------------------
# OUTPUT Paths

OUTPUT_DIR = BASE_DIR / "outputs"
FIGURES_DIR = OUTPUT_DIR / "figures"
REPORTS_DIR = OUTPUT_DIR / "reports"


# API SETTINGS
# =========================

EXCHANGE_RATE_API_BASE_URL = "https://v6.exchangerate-api.com/v6/EXCHANGE_RATE_API_KEY/latest/USD"

# Environment variable name (NOT the key itself)
EXCHANGE_RATE_API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")


# Default parameters

DEFAULT_CURRENCIES = ["EUR","GBP","SEK","QAR"]
REQUEST_TIMEOUT = 10