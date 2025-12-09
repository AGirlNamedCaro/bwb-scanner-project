# BWB Scanner

A Python module for scanning and ranking Broken Wing Butterfly (BWB) options spreads from CSV data.

## Overview

This project identifies viable Broken Wing Butterfly call spreads by:
1. Loading options chain data from CSV
2. Constructing all possible asymmetric BWB combinations
3. Filtering based on DTE, credit, and delta criteria
4. Ranking spreads by risk/reward ratio

## Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd bwb-scanner-project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Quick Start
Run the scanner on sample data:
```bash
python run_scanner.py
```

### Programmatic Usage
```python
from bwb_scanner.scanner import scan_bwbs

results = scan_bwbs(
    csv_path='data/sample_options.csv',
    min_dte=1,
    max_dte=10,
    min_credit=0.5,
    min_delta=0.20,
    max_delta=0.35
)

for result in results:
    print(result)
```

## Running Tests
```bash
pytest tests/ -v
```

## Project Structure
```
bwb-scanner-project/
├── bwb_scanner/
│   ├── __init__.py
│   ├── models.py              # OptionContract, BrokenWingButterfly
│   ├── calculators.py         # Payoff calculations
│   ├── spread_builder.py      # BWB construction logic
│   ├── filters.py             # DTE, credit, delta filters
│   ├── ranker.py              # Scoring and ranking
│   ├── data_loader.py         # CSV parsing
│   └── scanner.py             # Main orchestrator
├── tests/
│   ├── conftest.py            # Shared fixtures
│   ├── test_option_contract.py
│   ├── test_broken_wing_butterfly.py
│   ├── test_calculators.py
│   ├── test_spread_builder.py
│   ├── test_filters.py
│   ├── test_ranker.py
│   ├── test_data_loader.py
│   └── test_scanner.py
├── data/
│   └── sample_options.csv     # Sample options data
├── run_scanner.py             # CLI entry point
├── requirements.txt
└── README.md
```

## Assumptions
1. **Single ticker and expiry**: As per requirements, the scanner processes options for a single ticker and expiry. The sample CSV contains only AAPL options, and the scanner assumes all options share the same underlying and expiration date.

2. **Pre-filtered data**: The scanner assumes all options in the CSV have the same symbol, expiry, and type (all calls or all puts). Cross-symbol or mixed-type spreads are not validated.

3. **CSV format**: Expected columns are: `symbol, expiry, dte, strike, type, bid, ask, mid, delta, iv`

4. **Date format**: Expiry dates must be in `YYYY-MM-DD` format

5. **Score metric**: Spreads are ranked by `max_profit / max_loss` ratio. Higher is better.

## Design Decisions

- **TDD Approach**: All core functionality was built using test-driven development
- **Functional style**: Calculators and filters use pure functions for testability
- **Dataclasses**: Used for clean, immutable data structures
- **Single Responsibility**: Each module has one clear purpose
- **No external dependencies**: Uses only Python stdlib (except pytest for testing)

## Future Enhancements

### Additional Validations
- Validate same symbol/expiry/type across all BWB legs
- Add delta range validation (0-1 for calls, -1-0 for puts)
- Validate bid <= ask price ordering
- Check for negative DTE (expired options)

### Features
- Support for put BWBs
- Live market data integration (e.g., via broker API)
- Web interface for interactive scanning
- Export results to Excel/PDF

### Performance
- Optimize for large datasets (>10k options)
- Caching of calculated values

### Code Quality
- Add type hints throughout
- Increase test coverage to 100%
- Add integration tests with realistic market scenarios
- Refactor tests to use more fixtures (reduce duplication)
- Add more edge case tests

## Technical Notes

**Broken Wing Butterfly Structure:**
- Long 1 call at K1 (lower strike)
- Short 2 calls at K2 (middle strike)  
- Long 1 call at K3 (upper strike)
- Key: K2-K1 ≠ K3-K2 (asymmetric wings)

**Payoff Calculations:**
- Net Credit = 2×(K2 premium) - K1 premium - K3 premium
- Max Profit = Net Credit
- Max Loss = (Narrow wing width) - Net Credit
- Score = Max Profit / Max Loss