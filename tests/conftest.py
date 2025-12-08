# tests/conftest.py
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


@pytest.fixture
def option_contracts_valid_delta():
    """BWB with short delta in valid range (0.20-0.35)"""
    long_lower = OptionContract(
        symbol="AAPL",
        expiry=date(2023, 12, 15),
        strike=145.0,
        type="call",
        dte=5,
        bid=5.5,
        ask=6.5,
        mid=6.0,
        delta=0.6,
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
        delta=0.25,
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
        delta=0.15,
        iv=0.20,
    )

    return {
        "long_lower": long_lower,
        "short_middle": short_middle,
        "long_upper": long_upper,
    }


@pytest.fixture
def option_contracts_low_credit():
    """BWB with low net credit (< 1.0)"""
    long_lower = OptionContract(
        symbol="AAPL",
        expiry=date(2023, 12, 15),
        strike=145.0,
        type="call",
        dte=5,
        bid=4.5,
        ask=5.5,
        mid=5.0,
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
        bid=4.0,
        ask=5.0,
        mid=4.5,
        delta=0.3,
        iv=0.20,
    )

    return {
        "long_lower": long_lower,
        "short_middle": short_middle,
        "long_upper": long_upper,
    }


@pytest.fixture
def option_contracts_short_dte():
    """BWB with DTE too short (0 days)"""
    long_lower = OptionContract(
        symbol="AAPL",
        expiry=date(2023, 12, 15),
        strike=145.0,
        type="call",
        dte=0,
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
        dte=0,
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
        dte=0,
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


@pytest.fixture
def option_contracts_long_dte():
    """BWB with DTE too long (15 days)"""
    long_lower = OptionContract(
        symbol="AAPL",
        expiry=date(2024, 1, 15),
        strike=145.0,
        type="call",
        dte=15,
        bid=5.5,
        ask=6.5,
        mid=6.0,
        delta=0.7,
        iv=0.27,
    )

    short_middle = OptionContract(
        symbol="AAPL",
        expiry=date(2024, 1, 15),
        strike=150.0,
        type="call",
        dte=15,
        bid=4.5,
        ask=5.5,
        mid=5.0,
        delta=0.5,
        iv=0.25,
    )

    long_upper = OptionContract(
        symbol="AAPL",
        expiry=date(2024, 1, 15),
        strike=160.0,
        type="call",
        dte=15,
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


@pytest.fixture
def option_contracts_low_delta():
    """BWB with short delta too low (0.15)"""
    long_lower = OptionContract(
        symbol="AAPL",
        expiry=date(2023, 12, 15),
        strike=145.0,
        type="call",
        dte=5,
        bid=5.5,
        ask=6.5,
        mid=6.0,
        delta=0.5,
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
        delta=0.15,  # Too low!
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
        delta=0.1,
        iv=0.20,
    )

    return {
        "long_lower": long_lower,
        "short_middle": short_middle,
        "long_upper": long_upper,
    }


@pytest.fixture
def option_contracts_high_delta():
    """BWB with short delta too high (0.50)"""
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
        delta=0.50,  # Too high!
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
