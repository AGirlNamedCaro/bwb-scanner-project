from bwb_scanner.data_loader import load_options_from_csv
from bwb_scanner.spread_builder import build_spreads
from bwb_scanner.filters import filter_by_dte, filter_by_credit, filter_by_delta
from bwb_scanner.ranker import rank_bwbs


def scan_bwbs(csv_path, min_dte, max_dte, min_credit, min_delta, max_delta):
    option_contracts = load_options_from_csv(csv_path)
    bwbs = build_spreads(option_contracts)
    bwbs = filter_by_dte(bwbs, min_dte, max_dte)
    bwbs = filter_by_credit(bwbs, min_credit)
    bwbs = filter_by_delta(bwbs, min_delta, max_delta)
    ranked_bwbs = rank_bwbs(bwbs)
    return ranked_bwbs
