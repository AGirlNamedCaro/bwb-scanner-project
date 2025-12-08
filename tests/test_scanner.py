import pytest
from bwb_scanner.scanner import scan_bwbs


def test_scan_bwbs_end_to_end(tmp_path):
    csv_content = """symbol,expiry,dte,strike,type,bid,ask,mid,delta,iv
AAPL,2023-12-20,5,145.0,call,5.5,6.5,6.0,0.65,0.27
AAPL,2023-12-20,5,150.0,call,4.0,5.0,4.5,0.30,0.25
AAPL,2023-12-20,5,160.0,call,1.5,2.5,2.0,0.25,0.21
AAPL,2023-12-20,5,165.0,call,0.8,1.2,1.0,0.15,0.19
"""
    csv_file = tmp_path / "options.csv"
    csv_file.write_text(csv_content)

    results = scan_bwbs(
        str(csv_file),
        min_dte=1,
        max_dte=10,
        min_credit=0.5,
        min_delta=0.20,
        max_delta=0.35,
    )

    assert isinstance(results, list)
    assert len(results) > 0
    if len(results) > 1:
        assert results[0]["score"] >= results[1]["score"]
