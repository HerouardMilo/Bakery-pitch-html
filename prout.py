import threading
import time
import logging
from dotenv import load_dotenv
import os

from streaming.ingestion_logic import ingest_event
from streaming.flush_logic import flush
from streaming.simulator import run_simulator

load_dotenv()

log_path = os.getenv("log_path")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(f"{log_path}/streaming.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
env = os.getenv("ENV")

def run_flush_loop():
    '''
    Calls flush function every 5 sec
    '''
    while True :
        flush(env)
        time.sleep(5)
        
if __name__=="__main__":
    
    thread_simulator = threading.Thread(target=run_simulator, daemon=True)
    thread_flush = threading.Thread(target=run_flush_loop, daemon = True)
    
    thread_simulator.start()
    thread_flush.start()
    
    thread_simulator.join()
    thread_flush.join()
