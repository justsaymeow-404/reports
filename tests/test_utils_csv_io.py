from utils.csv_io import normalize_row, to_float


def test_normalize_row():
    row = {'  name  ': '  Alice   ', '  poSition ': '  Dev  '}
    out = normalize_row(row)
    assert out['name'] == 'Alice'
    assert out['position'] == 'Dev'


def test_to_float_parsig():
    assert to_float('1.5') == 1.5
    assert to_float('1,5') == 1.5
    assert to_float('  2  ') == 2.0
    assert to_float('') is None
    assert to_float(None) is None
    assert to_float('abc') is None
