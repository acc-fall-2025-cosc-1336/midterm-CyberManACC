def get_assessment_value(value: float) -> float:
    """Return the assessment value (60% of actual value)."""
    return round(0.60 * float(value), 2)


def get_tax_assessed(assessment_value: float) -> float:
    """
    Return the property tax at $0.72 per $100 of the assessment value.
    I.e., tax = assessment_value / 100 * 0.72
    """
    tax = (float(assessment_value) / 100.0) * 0.72
    return round(tax, 2)


# Optional: allow running this module directly for a quick demo
if __name__ == "__main__":
    print("Property Tax (type 'q' to quit)")
    while True:
        s = input("Enter actual property value: ").strip()
        if s.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            break
        try:
            actual = float(s)
        except ValueError:
            print("Please enter a valid number (e.g., 10000) or 'q' to quit.")
            continue
        assessed = get_assessment_value(actual)
        tax = get_tax_assessed(assessed)
        print(f"Assessed value: ${assessed:,.2f}  |  Tax assessed: ${tax:,.2f}")

