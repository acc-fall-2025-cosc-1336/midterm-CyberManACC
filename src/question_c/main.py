from question_c import get_assessment_value, get_tax_assessed

if __name__ == "__main__":
    print("Property Tax (type 'q' to quit)")
    while True:
        s = input("Enter Land Value: ").strip()
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
