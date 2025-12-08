from bwb_scanner.calculators import (
    calculate_max_profit,
    calculate_max_loss,
    calculate_net_credit,
)


def rank_bwbs(bwbs):
    results = []
    for bwb in bwbs:
        results.append(
            {
                "strikes": (
                    bwb.long_lower.strike,
                    bwb.short_middle.strike,
                    bwb.long_upper.strike,
                ),
                "credit": calculate_net_credit(bwb),
                "max_profit": calculate_max_profit(bwb),
                "max_loss": calculate_max_loss(bwb),
                "score": calculate_max_profit(bwb) / calculate_max_loss(bwb),
            }
        )
    return sorted(results, key=lambda x: x["score"], reverse=True)
