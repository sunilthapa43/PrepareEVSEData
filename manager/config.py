from dotenv import load_dotenv
import os

load_dotenv()

EVSE_NETWORK_PATH = os.environ.get('EVSE_NETWORK_ROOT')
EVSE_ROOT = os.environ.get('EVSE_ROOT')
OUTPUT_PATH = os.environ.get("OUTPUT_ROOT")