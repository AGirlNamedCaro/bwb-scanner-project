import pytest
from datetime import date
from bwb_scanner.data_loader import load_options_from_csv
from bwb_scanner.models import OptionContract


def test_load_options_from_csv(tmp_path):
    csv_content = """symbol,expiry,dte,strike,type,bid,ask,mid,delta,iv
AAPL,2023-12-15,5,145.0,call,5.5,6.5,6.0,0.7,0.27
AAPL,2023-12-15,5,150.0,call,4.5,5.5,5.0,0.5,0.25
AAPL,2023-12-15,5,160.0,call,1.5,2.5,2.0,0.3,0.20
"""
    csv_file = tmp_path / "test_options.csv"
    csv_file.write_text(csv_content)

    options = load_options_from_csv(str(csv_file))

    assert len(options) == 3
    assert all(isinstance(opt, OptionContract) for opt in options)
    assert options[0].symbol == "AAPL"
    assert options[0].expiry == date(2023, 12, 15)
    assert options[0].strike == 145.0
    assert options[0].type == "call"
