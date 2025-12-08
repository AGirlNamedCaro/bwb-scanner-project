from dataclasses import dataclass
from datetime import date


@dataclass
class OptionContract:
    symbol: str
    expiry: date
    dte: int
    strike: float
    type: str
    bid: float
    ask: float
    mid: float
    delta: float
    iv: float

    def __post_init__(self):
        if self.type not in ["call", "put"]:
            raise ValueError("type must be either 'call' or 'put'")
        if self.strike <= 0:
            raise ValueError("strike must be a positive number")


@dataclass
class BrokenWingButterfly:
    long_lower: OptionContract
    short_middle: OptionContract
    long_upper: OptionContract

    def __post_init__(self):
        lower_wing_width = self.short_middle.strike - self.long_lower.strike
        upper_wing_width = self.long_upper.strike - self.short_middle.strike
        if lower_wing_width == upper_wing_width:
            raise ValueError(
                "The wings must be asymmetric for a broken-wing butterfly."
            )
        if not (
            self.long_lower.strike < self.short_middle.strike < self.long_upper.strike
        ):
            raise ValueError("Strikes are out of order")
