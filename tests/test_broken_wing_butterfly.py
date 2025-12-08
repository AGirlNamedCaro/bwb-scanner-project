from datetime import date
import pytest
from bwb_scanner.models import OptionContract, BrokenWingButterfly


def test_create_bwb_with_valid_options():
    long_lower = OptionContract(
        symbol="AAPL",
        expiry=date(2023, 12, 15),
        strike=145.0,
        type="call",
        dte=5,
        bid=5.5,
        ask=6.5,
        mid=6.0,
        delta=0.7,
        iv=0.27,
    )

    short_middle = OptionContract(
        symbol="AAPL",
        expiry=date(2023, 12, 15),
        strike=150.0,
        type="call",
        dte=5,
        bid=4.5,
        ask=5.5,
        mid=5.0,
        delta=0.6,
        iv=0.25,
    )

    # K3 = 160 (long 1)
    long_upper = OptionContract(
        symbol="AAPL",
        expiry=date(2023, 12, 15),
        strike=160.0,
        type="call",
        dte=5,
        bid=1.5,
        ask=2.5,
        mid=2.0,
        delta=0.3,
        iv=0.20,
    )

    bwb = BrokenWingButterfly(
        long_lower=long_lower, short_middle=short_middle, long_upper=long_upper
    )

    assert bwb.long_lower == long_lower
    assert bwb.short_middle == short_middle
    assert bwb.long_upper == long_upper


def test_bwb_rejects_symmetric_wings():
    long_lower = OptionContract(
        symbol="AAPL",
        expiry=date(2023, 12, 15),
        strike=145.0,
        type="call",
        dte=5,
        bid=5.5,
        ask=6.5,
        mid=6.0,
        delta=0.7,
        iv=0.27,
    )

    short_middle = OptionContract(
        symbol="AAPL",
        expiry=date(2023, 12, 15),
        strike=150.0,
        type="call",
        dte=5,
        bid=4.5,
        ask=5.5,
        mid=5.0,
        delta=0.6,
        iv=0.25,
    )

    long_upper = OptionContract(
        symbol="AAPL",
        expiry=date(2023, 12, 15),
        strike=155.0,
        type="call",
        dte=5,
        bid=1.5,
        ask=2.5,
        mid=2.0,
        delta=0.3,
        iv=0.20,
    )

    with pytest.raises(
        ValueError, match="The wings must be asymmetric for a broken-wing butterfly."
    ):
        BrokenWingButterfly(
            long_lower=long_lower, short_middle=short_middle, long_upper=long_upper
        )


def test_bwb_rejects_strikes_out_of_order():
    long_lower = OptionContract(
        symbol="AAPL",
        expiry=date(2023, 12, 15),
        strike=155.0,
        type="call",
        dte=5,
        bid=5.5,
        ask=6.5,
        mid=6.0,
        delta=0.7,
        iv=0.27,
    )

    short_middle = OptionContract(
        symbol="AAPL",
        expiry=date(2023, 12, 15),
        strike=150.0,
        type="call",
        dte=5,
        bid=4.5,
        ask=5.5,
        mid=5.0,
        delta=0.6,
        iv=0.25,
    )

    long_upper = OptionContract(
        symbol="AAPL",
        expiry=date(2023, 12, 15),
        strike=160.0,
        type="call",
        dte=5,
        bid=1.5,
        ask=2.5,
        mid=2.0,
        delta=0.3,
        iv=0.20,
    )

    with pytest.raises(ValueError, match="Strikes are out of order"):
        BrokenWingButterfly(
            long_lower=long_lower,
            short_middle=short_middle,
            long_upper=long_upper,
        )
