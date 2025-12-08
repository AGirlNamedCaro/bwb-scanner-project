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
