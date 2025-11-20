import json
import logging
from pathlib import Path

from etl.extract import extract
from etl.transform import transform
from etl.load import load


def load_config(config_path: str = "config.json") -> dict:
    """
    Load configuration from a JSON file.

    Parameters
    ----------
    config_path : str
        Path to the JSON config file.

    Returns
    -------
    dict
        Parsed configuration.
    """
    config_file = Path(config_path)
    if not config_file.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with config_file.open("r", encoding="utf-8") as f:
        return json.load(f)


def setup_logging(config: dict) -> None:
    """
    Configure logging using values from config.

    Parameters
    ----------
    config : dict
        Configuration dictionary containing log_path and log_level.
    """
    log_path = Path(config["log_path"])
    log_path.parent.mkdir(parents=True, exist_ok=True)

    log_level_name = config.get("log_level", "INFO").upper()
    log_level = getattr(logging, log_level_name, logging.INFO)

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


def run_etl() -> None:
    # 1. Load configuration
    config = load_config()

    # 2. Setup logging using config values
    setup_logging(config)

    logger = logging.getLogger(__name__)
    logger.info("Starting ETL pipeline...")

    try:
        # Extract
        raw_data = extract(
            source=config["source"],
            input_path=config["input_path"],
            api_url=config["api_url"],
        )

        # Transform
        transformed_data = transform(raw_data)

        # Load
        load(transformed_data, output_path=config["output_path"])

        logger.info("ETL pipeline finished successfully")
    except Exception:
        logger.exception("ETL pipeline failed")
        raise


if __name__ == "__main__":
    run_etl()
