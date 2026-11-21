import json
from pathlib import Path

from models import Car

DATA_FILE = Path('data.json')

def load_cars() -> list[Car]:
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            raw = json.load(f)
        return [Car.from_dict(item) for item in raw]

    except (json.JSONDecodeError, KeyError, TypeError) as e:
        print(f'[ERROR]: {e}')
        return []

def save_cars(cars: list[Car]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump([c.to_dict() for c in cars], f, ensure_ascii=False, indent=2)