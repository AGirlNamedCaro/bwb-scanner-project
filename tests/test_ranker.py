import pytest
from bwb_scanner.models import BrokenWingButterfly
from bwb_scanner.ranker import rank_bwbs


def test_rank_bwbs_returns_sorted_results_with_metrics(
    option_contracts_asym, option_contracts_low_credit
):
    bwb_high_score = BrokenWingButterfly(**option_contracts_asym)
    bwb_low_score = BrokenWingButterfly(**option_contracts_low_credit)

    bwbs = [bwb_low_score, bwb_high_score]

    ranked = rank_bwbs(bwbs)

    assert len(ranked) == 2
    assert isinstance(ranked[0], dict)

    assert ranked[0]["strikes"] == (145.0, 150.0, 160.0)
    assert ranked[0]["credit"] == 2.0
    assert ranked[0]["max_profit"] == 2.0
    assert ranked[0]["max_loss"] == 3.0
    assert ranked[0]["score"] == pytest.approx(0.6667, rel=0.01)

    assert ranked[1]["score"] < ranked[0]["score"]
