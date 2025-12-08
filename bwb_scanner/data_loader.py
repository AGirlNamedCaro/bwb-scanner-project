import csv
from datetime import datetime
from bwb_scanner.models import OptionContract


def load_options_from_csv(file_path: str) -> list:

    options = []
    with open(file_path, mode="r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            option = OptionContract(
                symbol=row["symbol"],
                expiry=datetime.strptime(row["expiry"], "%Y-%m-%d").date(),
                dte=int(row["dte"]),
                strike=float(row["strike"]),
                type=row["type"],
                bid=float(row["bid"]),
                ask=float(row["ask"]),
                mid=float(row["mid"]),
                delta=float(row["delta"]),
                iv=float(row["iv"]),
            )
            options.append(option)
    return options
