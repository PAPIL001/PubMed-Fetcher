# PubMed Paper Fetcher

## Overview
This project provides a Python script to fetch research papers from PubMed based on a given search query. It extracts details such as the title, publication date, non-academic authors (company-affiliated), company affiliations, and corresponding author emails.

## Project Structure
- `fetch_pubmed.py` - Main script for fetching PubMed papers.
- `requirements.txt` - List of dependencies for the project.
- `README.md` - Documentation for installation and usage.

## Installation
### Prerequisites
Ensure you have Python installed (version 3.10 or later).

### Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/PAPIL001/PubMed-Fetcher.git
   cd PubMed-Fetcher
   ```
2. Install Poetry (if not already installed):
   ```sh
   pip install poetry
   ```
3. Install dependencies using Poetry:
   ```sh
   poetry install
   ```
   Or use pip:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the script with a search query:
```sh
python fetch_pubmed.py "cancer treatment"
```

### Additional Options
- **Debug Mode:**
  ```sh
  python fetch_pubmed.py "cancer treatment" --debug
  ```
  Prints detailed output for debugging.
- **Save to CSV:**
  ```sh
  python fetch_pubmed.py "cancer treatment" -f results.csv
  ```
  Saves the output to `results.csv`.

### Example Output
```json
[
  {
    "PubmedID": "40064621",
    "Title": "Adding New Components to a Composite Quality Metric: How Good Is Good Enough?",
    "Publication Date": "2025",
    "Non-academic Author(s)": "N/A",
    "Company Affiliation(s)": "N/A",
    "Corresponding Author Email": "N/A"
  }
]
```

## Tools and Libraries Used
- **PubMed E-utilities API** ([Documentation](https://www.ncbi.nlm.nih.gov/books/NBK25500/))
- **Python Standard Libraries:** `requests`, `csv`, `argparse`, `xml.etree.ElementTree`, `re`
- **Dependency Management:** Poetry ([Poetry Docs](https://python-poetry.org/))
- **Version Control:** GitHub


