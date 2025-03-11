import requests
import csv
import re
import argparse
import xml.etree.ElementTree as ET
from typing import List, Dict, Any

def fetch_pubmed_papers(query: str) -> List[Dict[str, Any]]:
    """
    Fetch papers from PubMed based on the given query.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10  # Fetch only top 10 results for now
    }
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        raise Exception("Failed to fetch data from PubMed API")
    
    paper_ids = response.json().get("esearchresult", {}).get("idlist", [])
    
    return fetch_paper_details(paper_ids)

def fetch_paper_details(paper_ids: List[str]) -> List[Dict[str, Any]]:
    """
    Fetch detailed information about the papers using their PubMed IDs.
    """
    details_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "xml"
    }
    response = requests.get(details_url, params=params)
    if response.status_code != 200:
        raise Exception("Failed to fetch paper details")
    
    root = ET.fromstring(response.text)
    papers = []
    
    for article in root.findall(".//PubmedArticle"):
        pmid = article.find(".//PMID").text if article.find(".//PMID") is not None else "N/A"
        title = article.find(".//ArticleTitle").text if article.find(".//ArticleTitle") is not None else "N/A"
        
        pub_date = article.find(".//PubDate/Year")
        if pub_date is not None:
            pub_date = pub_date.text
        else:
            medline_date = article.find(".//PubDate/MedlineDate")
            pub_date = medline_date.text if medline_date is not None else "N/A"
        
        authors = []
        company_affiliations = set()
        emails = set()
        
        for author in article.findall(".//Author"):
            last_name = author.find("LastName")
            last_name_text = last_name.text if last_name is not None else "N/A"
            affiliation_info = author.findall(".//AffiliationInfo")
            
            for aff in affiliation_info:
                affiliation = aff.find("Affiliation")
                if affiliation is not None:
                    aff_text = affiliation.text
                    if aff_text:
                        # Identify company affiliations with a broader keyword set
                        company_keywords = ["inc", "corp", "company", "pharma", "biotech", "ltd", "gmbh", "s.a.", "plc", "llc", "co.", "industries", "labs", "systems", "technologies", "research institute", "consulting", "solutions", "medical center"]
                        if any(keyword in aff_text.lower() for keyword in company_keywords):
                            authors.append(last_name_text)
                            company_affiliations.add(aff_text)
                        
                        # Extract email addresses
                        found_emails = re.findall(r"[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}", aff_text)
                        emails.update(found_emails)
        
        papers.append({
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": ", ".join(authors) if authors else "N/A",
            "Company Affiliation(s)": ", ".join(company_affiliations) if company_affiliations else "N/A",
            "Corresponding Author Email": ", ".join(emails) if emails else "N/A"
        })
    
    return papers

def save_to_csv(papers: List[Dict[str, Any]], filename: str):
    """
    Save the list of papers to a CSV file.
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"])
        writer.writeheader()
        writer.writerows(papers)

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed based on a query.")
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug information.")
    parser.add_argument("-f", "--file", type=str, help="Save results to a CSV file.")
    
    args = parser.parse_args()
    
    papers = fetch_pubmed_papers(args.query)
    
    if args.debug:
        print("Fetched Papers:", papers)
    
    if args.file:
        save_to_csv(papers, args.file)
        print(f"Results saved to {args.file}")
    else:
        print(papers)

if __name__ == "__main__":
    main()
