from bwb_scanner.calculators import calculate_net_credit


def filter_by_credit(bwbs, min_credit):
    filtered_bwbs = []
    for bwb in bwbs:
        net_credit = calculate_net_credit(bwb)
        if net_credit >= min_credit:
            filtered_bwbs.append(bwb)
    return filtered_bwbs


def filter_by_dte(bwbs, min_dte, max_dte):
    filtered_bwbs = []
    for bwb in bwbs:
        dte = bwb.short_middle.dte
        if min_dte <= dte <= max_dte:
            filtered_bwbs.append(bwb)
    return filtered_bwbs


def filter_by_delta(bwbs, min_delta, max_delta):
    filtered_bwbs = []
    for bwb in bwbs:
        delta = abs(bwb.short_middle.delta)
        if min_delta <= delta <= max_delta:
            filtered_bwbs.append(bwb)
    return filtered_bwbs
