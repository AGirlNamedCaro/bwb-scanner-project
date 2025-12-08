def calculate_net_credit(bwb):
    long_lower_premium = bwb.long_lower.mid
    short_middle_premium = bwb.short_middle.mid
    long_upper_premium = bwb.long_upper.mid

    net_credit = (2 * short_middle_premium) - long_lower_premium - long_upper_premium
    return net_credit


def calculate_max_profit(bwb):
    return calculate_net_credit(bwb)


def calculate_max_loss(bwb):
    narrow_wing_width = min(
        bwb.short_middle.strike - bwb.long_lower.strike,
        bwb.long_upper.strike - bwb.short_middle.strike,
    )

    return narrow_wing_width - calculate_net_credit(bwb)
