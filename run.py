from collectors.cisa import get_cisa_kev


def main():
    print("\nBLACKWATCH AI")
    print("Known Exploited Vulnerabilities Feed")
    print("=" * 70)

    kev_items = get_cisa_kev(limit=10)

    for item in kev_items:
        print(f"\n{item['id']} | {item['vendor']} {item['product']}")
        print(f"Name: {item['name']}")
        print(f"Date Added: {item['date_added']}")
        print(f"Due Date: {item['due_date']}")
        print(f"Required Action: {item['action']}")


if __name__ == "__main__":
    main()
    
