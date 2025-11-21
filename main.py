import argparse
import sys

from tabulate import tabulate

from reports import get_report
from utils.csv_io import read_rows_from_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Генерация отчетов')
    parser.add_argument('--files', nargs='+', required=True, help='Путь к файлам')
    parser.add_argument('--report', required=True, help='Название отчета')
    return parser.parse_args()


def main():
    args = parse_args()
    report = get_report(args.report)
    assert report is not None, 'Отчет не найден.'

    rows = read_rows_from_files(args.files)
    if not rows:
        print('Нет данных для обработки (проверьте файлы).', file=sys.stderr)
        sys.exit(1)
    
    headers, data = report.compute(rows=rows)
    
    if not data:
        print('Нет данных для отчета', file=sys.stderr)
        sys.exit(0)
    
    print(tabulate(data, headers=headers, tablefmt='simple'))


if __name__ == '__main__':
    main()
