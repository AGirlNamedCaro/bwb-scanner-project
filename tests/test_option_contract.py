import pytest
from datetime import date
from bwb_scanner.models import OptionContract


def test_create_option_contract_with_valid_data():
    option_data = {
        "symbol": "AAPL",
        "expiry": date.date(2023, 12, 15),
        "strike": 150.0,
        "type": "call",
        "dte": 30,
        "bid": 4.5,
        "ask": 5.5,
        "mid": 5.0,
        "delta": 0.6,
        "iv": 0.25,
    }

    option_contract = OptionContract(**option_data)

    assert option_contract.symbol == "AAPL"
    assert option_contract.expiry == date.date(2023, 12, 15)
    assert option_contract.strike == 150.0
    assert option_contract.type == "call"
    assert option_contract.dte == 30
    assert option_contract.bid == 4.5
    assert option_contract.ask == 5.5
    assert option_contract.mid == 5.0
    assert option_contract.delta == 0.6
    assert option_contract.iv == 0.25


def test_option_contract_rejects_invalid_type():
    option_data = {
        "symbol": "AAPL",
        "expiry": date.date(2023, 12, 15),
        "strike": 150.0,
        "type": "invalid_type",
        "dte": 30,
        "bid": 4.5,
        "ask": 5.5,
        "mid": 5.0,
        "delta": 0.6,
        "iv": 0.25,
    }

    with pytest.raises(ValueError, match="type must be either 'call' or 'put'"):
        OptionContract(**option_data)


def test_option_contract_rejects_negative_strike():
    option_data = {
        "symbol": "AAPL",
        "expiry": date.date(2023, 12, 15),
        "strike": -150.0,
        "type": "call",
        "dte": 30,
        "bid": 4.5,
        "ask": 5.5,
        "mid": 5.0,
        "delta": 0.6,
        "iv": 0.25,
    }

    with pytest.raises(ValueError, match="strike must be a positive number"):
        OptionContract(**option_data)
