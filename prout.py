import threading
import time
import logging
from dotenv import load_dotenv
import os

from streaming.ingestion_logic import ingest_event
from streaming.flush_logic import flush
from streaming.simulator import run_simulator

load_dotenv()

logger = logging.getLogger(__name__)
log_path = os.getenv("log_path")

logging.basicConfig(
    filename=f"{log_path}/streaming/thread_manager.py.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

env = os.getenv("ENV")
