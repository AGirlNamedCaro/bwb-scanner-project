import pytest
from datetime import date
from bwb_scanner.models import OptionContract


@pytest.fixture
def option_contracts_asym():
    """Create sample option contracts for testing BWB"""
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
        delta=0.5,
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

    return {
        "long_lower": long_lower,
        "short_middle": short_middle,
        "long_upper": long_upper,
    }
