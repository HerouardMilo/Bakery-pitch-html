import time
import random
import logging
from datetime import datetime
from streaming.ingestion_logic import ingest_event

logger = logging.getLogger(__name__)

PRODUITS = ["P-001", "P-002", "P-003", "P-004", "P-005"]
CLIENTS = ["C-001", "C-002", "C-003", "C-004", None]
REGLEMENTS = ["CB", "especes", "ticket_resto"]

def generate_event() -> dict:
    '''
    Generates a fake POS event
    Args:
        None
    Returns:
        event : dict representing a single POS transaction
    '''
    return {
        "id_vente": f"V-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000,9999)}",
        "id_produit": random.choice(PRODUITS),
        "quantite": random.randint(1, 5),
        "prix_unitaire_ttc": round(random.uniform(0.90, 8.50), 2),
        "remise_pct": random.choice([0.0, 0.0, 0.0, 5.0, 10.0]),
        "sur_place": random.choice([True, False]),
        "id_client": random.choice(CLIENTS),
        "type_reglement": random.choice(REGLEMENTS),
        "timestamp": datetime.now().isoformat()
    }

def run_simulator(interval_sec: float = 2.0) -> None:
    '''
    Continuously generates fake POS events and pushes them to the queue
    Args:
        interval_sec : seconds between each event
    Returns:
        None
    '''
    logger.info("Simulator started")
    while True:
        event = generate_event()
        ingest_event(event)
        logger.debug(f"Event simulated: {event['id_vente']}")
        time.sleep(interval_sec)
