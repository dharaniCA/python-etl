import csv
import logging
from pathlib import Path
from typing import List, Dict, Any

import requests

logger = logging.getLogger(__name__)


def extract_from_csv(input_path: str) -> List[Dict[str, Any]]:
    input_file = Path(input_path)

    if not input_file.exists():
        logger.error("Input CSV file does not exist: %s", input_path)
        raise FileNotFoundError(f"Input file not found: {input_path}")

    records: List[Dict[str, Any]] = []
    try:
        with input_file.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["age"] = int(row["age"])
                records.append(row)

        logger.info("Extracted %d records from CSV: %s", len(records), input_path)
        return records
    except Exception:
        logger.exception("Failed to extract data from CSV: %s", input_path)
        raise


def extract_from_api(api_url: str) -> List[Dict[str, Any]]:
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        payload = response.json()
    except Exception:
        logger.exception("Failed to fetch data from API: %s", api_url)
        raise

    records: List[Dict[str, Any]] = []
    for item in payload:
        record = {
            "name": item.get("name", "Unknown"),
            # fake age just for demo, using id
            "age": int(item.get("id", 0)) + 20
        }
        records.append(record)

    logger.info("Extracted %d records from API: %s", len(records), api_url)
    return records


def extract(source: str, input_path: str, api_url: str):
    if source == "csv":
        return extract_from_csv(input_path)
    elif source == "api":
        return extract_from_api(api_url)
    else:
        raise ValueError(f"Unsupported source type: {source}")
