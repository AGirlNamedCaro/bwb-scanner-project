# tests/test_filters.py
import pytest
from bwb_scanner.models import BrokenWingButterfly
from bwb_scanner.filters import filter_by_credit, filter_by_dte, filter_by_delta


def test_filter_by_credit_removes_low_credit_bwbs(
    option_contracts_asym, option_contracts_low_credit
):
    bwb_high_credit = BrokenWingButterfly(**option_contracts_asym)
    bwb_low_credit = BrokenWingButterfly(**option_contracts_low_credit)

    bwbs = [bwb_high_credit, bwb_low_credit]
    filtered = filter_by_credit(bwbs, min_credit=1.0)

    assert len(filtered) == 1
    assert filtered[0] == bwb_high_credit


def test_filter_by_dte_removes_out_of_range_bwbs(
    option_contracts_asym, option_contracts_short_dte, option_contracts_long_dte
):
    bwb_valid_dte = BrokenWingButterfly(**option_contracts_asym)
    bwb_too_short = BrokenWingButterfly(**option_contracts_short_dte)
    bwb_too_long = BrokenWingButterfly(**option_contracts_long_dte)

    bwbs = [bwb_valid_dte, bwb_too_short, bwb_too_long]
    filtered = filter_by_dte(bwbs, min_dte=1, max_dte=10)

    assert len(filtered) == 1
    assert filtered[0] == bwb_valid_dte


def test_filter_by_delta_removes_out_of_range_bwbs(
    option_contracts_valid_delta,
    option_contracts_low_delta,
    option_contracts_high_delta,
):
    bwb_valid_delta = BrokenWingButterfly(**option_contracts_valid_delta)
    bwb_too_low = BrokenWingButterfly(**option_contracts_low_delta)
    bwb_too_high = BrokenWingButterfly(**option_contracts_high_delta)

    bwbs = [bwb_valid_delta, bwb_too_low, bwb_too_high]
    filtered = filter_by_delta(bwbs, min_delta=0.20, max_delta=0.35)

    assert len(filtered) == 1
    assert filtered[0] == bwb_valid_delta
