import requests


CISA_KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"


def get_cisa_kev(limit=10):
    try:
        response = requests.get(CISA_KEV_URL, timeout=15)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as error:
        print(f"Error fetching CISA KEV data: {error}")
        return []

    vulnerabilities = data.get("vulnerabilities", [])

    kev_items = []

    for item in vulnerabilities[:limit]:
        kev_items.append({
            "id": item.get("cveID", "Unknown CVE"),
            "vendor": item.get("vendorProject", "Unknown vendor"),
            "product": item.get("product", "Unknown product"),
            "name": item.get("vulnerabilityName", "Unknown vulnerability"),
            "date_added": item.get("dateAdded", "Unknown date"),
            "due_date": item.get("dueDate", "Unknown due date"),
            "action": item.get("requiredAction", "No action provided."),
            "source": "CISA KEV"
        })

    return kev_items
