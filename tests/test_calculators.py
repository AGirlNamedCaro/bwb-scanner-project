from datetime import date
from bwb_scanner.models import OptionContract, BrokenWingButterfly
from bwb_scanner.calculators import (
    calculate_net_credit,
    calculate_max_profit,
    calculate_max_loss,
)


def test_calculate_net_credit(option_contracts_asym):
    bwb = BrokenWingButterfly(
        long_lower=option_contracts_asym["long_lower"],
        short_middle=option_contracts_asym["short_middle"],
        long_upper=option_contracts_asym["long_upper"],
    )

    credit = calculate_net_credit(bwb)
    assert credit == 2.0


def test_calculate_max_profit(option_contracts_asym):
    bwb = BrokenWingButterfly(
        long_lower=option_contracts_asym["long_lower"],
        short_middle=option_contracts_asym["short_middle"],
        long_upper=option_contracts_asym["long_upper"],
    )

    max_profit = calculate_max_profit(bwb)
    assert max_profit == 2.0
    assert max_profit == calculate_net_credit(bwb)


def test_calculate_max_loss(option_contracts_asym):
    bwb = BrokenWingButterfly(
        long_lower=option_contracts_asym["long_lower"],
        short_middle=option_contracts_asym["short_middle"],
        long_upper=option_contracts_asym["long_upper"],
    )

    max_loss = calculate_max_loss(bwb)
    assert max_loss == 3.0
