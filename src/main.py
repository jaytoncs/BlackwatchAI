import os
from dotenv import load_dotenv
import requests
import pandas as pd

load_dotenv()

API_URL = os.getenv("API_URL", "https://jsonplaceholder.typicode.com/posts")


def fetch_posts(url=API_URL):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def make_dataframe(data):
    return pd.DataFrame(data)


def main():
    data = fetch_posts()
    df = make_dataframe(data)
    print(df.head())


if __name__ == "__main__":
    main()
import requests
from datetime import datetime


def get_recent_cves(limit=10):
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage={limit}"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as error:
        print(f"Error fetching CVE data: {error}")
        return []

    threats = []

    for item in data.get("vulnerabilities", []):
        cve = item.get("cve", {})

        cve_id = cve.get("id", "Unknown CVE")
        published = cve.get("published", "Unknown date")
        description = cve.get("descriptions", [{}])[0].get("value", "No description available.")

        metrics = cve.get("metrics", {})
        severity = "Unknown"
        score = "N/A"

        if "cvssMetricV31" in metrics:
            cvss = metrics["cvssMetricV31"][0]["cvssData"]
            severity = cvss.get("baseSeverity", "Unknown")
            score = cvss.get("baseScore", "N/A")
        elif "cvssMetricV30" in metrics:
            cvss = metrics["cvssMetricV30"][0]["cvssData"]
            severity = cvss.get("baseSeverity", "Unknown")
            score = cvss.get("baseScore", "N/A")

        threats.append({
            "id": cve_id,
            "published": published,
            "severity": severity,
            "score": score,
            "description": description
        })

    return threats


def print_briefing(threats):
    print("\nBLACKWATCH AI")
    print("Autonomous Threat Intelligence Briefing System")
    print("=" * 60)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Threats analyzed: {len(threats)}")
    print("=" * 60)

    for threat in threats:
        print(f"\n{threat['id']}")
        print(f"Published: {threat['published']}")
        print(f"Severity: {threat['severity']} | CVSS Score: {threat['score']}")
        print(f"Summary: {threat['description'][:350]}...")


def main():
    threats = get_recent_cves(limit=10)
    print_briefing(threats)


if __name__ == "__main__":
    main()
    
