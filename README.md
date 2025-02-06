# Talos Pinkhat CTA STIX Extensions

This project defines a custom STIX2 extension for analysis engine artifacts and demonstrates its usage with a MalwareAnalysis example.

## Installation

To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage

The main module `cta/analysis.py` defines a custom STIX2 extension and demonstrates its usage. You can run the module to see an example of the extension in action:
```bash
python cta/analysis.py
```

## Testing

To run the tests, use `pytest`:
```bash
pytest tests/test_analysis.py
```

## Project Structure

- `cta/analysis.py`: Defines the custom STIX2 extension and demonstrates its usage.
- `tests/test_analysis.py`: Contains tests for the custom STIX2 extension.

# stix-extensions

Prototypes and new potential STIX extensions.
