from bwb_scanner.scanner import scan_bwbs
import json


def main():
    print("Running BWB Scanner...")
    print("=" * 50)

    results = scan_bwbs(
        csv_path="data/sample_options.csv",
        min_dte=1,
        max_dte=10,
        min_credit=0.5,
        min_delta=0.20,
        max_delta=0.35,
    )

    print(f"\nFound {len(results)} viable BWB spreads:\n")

    for i, result in enumerate(results, 1):
        print(f"Rank #{i}")
        print(f"  Strikes (K1, K2, K3): {result['strikes']}")
        print(f"  Net Credit: ${result['credit']:.2f}")
        print(f"  Max Profit: ${result['max_profit']:.2f}")
        print(f"  Max Loss: ${result['max_loss']:.2f}")
        print(f"  Score (Profit/Loss): {result['score']:.4f}")
        print()


if __name__ == "__main__":
    main()
