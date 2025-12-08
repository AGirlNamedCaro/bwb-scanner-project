from itertools import combinations
from bwb_scanner.models import BrokenWingButterfly


def build_spreads(options):
    bwbs = []
    sorted_options = sorted(options, key=lambda o: o.strike)
    option_combos = combinations(sorted_options, 3)
    for long_lower, short_middle, long_upper in option_combos:
        try:
            bwb = BrokenWingButterfly(
                long_lower=long_lower,
                short_middle=short_middle,
                long_upper=long_upper,
            )
            bwbs.append(bwb)
        except ValueError:
            pass
    return bwbs
