import json
from pathlib import Path


def load(data, output_path="data/output.json"):
    """
    Load step:
    - Save the transformed data to a JSON file in the data/ folder.
    """
    # Make sure the directory exists
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
