# PubMed Paper Fetcher  

## Overview  
This project provides a Python script to fetch research papers from PubMed based on a given search query. It extracts details such as the title, publication date, non-academic authors (company-affiliated), company affiliations, and corresponding author emails.  

## Project Structure  
- `fetch_pubmed.py` - Main script for fetching PubMed papers.  
- `requirements.txt` - List of dependencies for the project.  
- `pyproject.toml` - Poetry configuration file for dependency management.  
- `README.md` - Documentation for installation and usage.  
- `pubmed_results.csv` - Sample output file (optional).  

## Installation  

### Prerequisites  
Ensure you have Python installed (version 3.10 or later).  

### Steps  
1. Clone this repository:  
   ```sh
   git clone https://github.com/PAPIL001/PubMed-Fetcher.git
   cd PubMed-Fetcher
Install Poetry (if not already installed):
sh
Copy
Edit
pip install poetry
Install dependencies using Poetry:
sh
Copy
Edit
poetry install
Or use pip:
sh
Copy
Edit
pip install -r requirements.txt
Usage
Run the script with a search query:

sh
Copy
Edit
python fetch_pubmed.py "cancer treatment"
Additional Options
Debug Mode:
sh
Copy
Edit
python fetch_pubmed.py "cancer treatment" --debug
Prints detailed output for debugging.
Save to CSV:
sh
Copy
Edit
python fetch_pubmed.py "cancer treatment" -f results.csv
Saves the output to results.csv.
Example Output
json
Copy
Edit
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
Tools and Libraries Used
PubMed E-utilities API (Documentation)
Python Standard Libraries: requests, csv, argparse, xml.etree.ElementTree, re
Dependency Management: Poetry (Poetry Docs)
Version Control: GitHub
vbnet
Copy
Edit

This is a clean and structured version of **README.md**. Let me know if you need any changes! 🚀






