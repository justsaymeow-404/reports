import argparse
from collections import defaultdict
from typing import Optional

from utils.csv_io import to_float


class Report:
    name: str = ""
    description = ""

    def compute(self, rows: list[dict[str, str]]) -> tuple[list[str], list[tuple]]:
        raise NotImplementedError


REPORTS: dict[str, Report] = {}


def register_report(report: Report):
    if not report.name:
        raise ValueError('У отчета должно быть имя')
    key = report.name.lower()
    REPORTS[key] = report


def get_report(name:str) -> Optional[Report]:
    key = name.lower()
    if key in REPORTS:
        return REPORTS[key]
    return None


class PerformanceReport(Report):
    name = 'performance'
    description = 'Средняя эффективность по позициям'

    def compute(self, rows: list[dict]) -> tuple[tuple[str], list[tuple]]:
        agg_sum: dict[str, float] = defaultdict(float)
        agg_count: dict[str, int] = defaultdict(int)
        for r in rows:
            agg_sum[r['position']] += to_float(r['performance'])
            agg_count[r['position']] += 1

        table: list[list] = []
        for position in agg_sum.keys():
            avg = agg_sum[position] / agg_count[position] if agg_count[position] else 0.0
            table.append((position, round(avg, 2)))
        
        headers = ('position', 'performance')
        return headers, sorted(table, key=lambda item: item[1], reverse=True)


register_report(PerformanceReport())
