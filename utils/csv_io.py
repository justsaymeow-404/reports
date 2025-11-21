import csv
import sys

from typing import Optional


def normalize_key(key: str) -> str:
    return key.strip().lower()


def normalize_row(row: dict[str, str]) -> dict[str, str]:
    return {normalize_key(k): (v.strip() if isinstance(v, str) else v) for k, v in row.items()}


def to_float(value: str) -> Optional[float]:
    if value is None:
        return None
    s = str(value).strip().replace(',', '.')
    try:
        return float(s)
    except (ValueError, TypeError):
        return None


def read_rows_from_files(files: list[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in files:
        try:
            with open(path, 'r', encoding='utf-8', newline='\n') as f:
                reader = csv.DictReader(f)
                if reader.fieldnames is None:
                    print(f'Файл {path} не содержит заголовка.', file=sys.stderr)
                    continue
                for raw in reader:
                    rows.append(normalize_row(raw))
        except FileNotFoundError:
            print(f'Файл {path} не найден.', file=sys.stderr)
        except Exception as e:
            print(f'Ошибка чтения {path}: {e}', file=sys.stderr)
    return rows
