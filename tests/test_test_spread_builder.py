from datetime import date
from bwb_scanner.models import OptionContract
from bwb_scanner.spread_builder import build_spreads


def test_build_spreads_creates_only_asymmetric_bwbs(option_contracts_asym):
    option4 = OptionContract(
        symbol="AAPL",
        expiry=date(2023, 12, 15),
        strike=155.0,
        type="call",
        dte=5,
        bid=3.0,
        ask=4.0,
        mid=3.5,
        delta=0.4,
        iv=0.22,
    )
    options = [
        option_contracts_asym["long_lower"],
        option_contracts_asym["short_middle"],
        option_contracts_asym["long_upper"],
        option4,
    ]

    bwbs = build_spreads(options)
    expected_strikes = {(145.0, 150.0, 160.0), (145.0, 155.0, 160.0)}
    actual_strikes = {
        (bwb.long_lower.strike, bwb.short_middle.strike, bwb.long_upper.strike)
        for bwb in bwbs
    }
    assert len(bwbs) == 2
    assert actual_strikes == expected_strikes
