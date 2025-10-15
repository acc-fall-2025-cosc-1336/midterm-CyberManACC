from question_d import get_person_category

if __name__ == "__main__":
    print("Age Category Checker (type 'q' to quit)")
    while True:
        raw = input("Enter age: ").strip().lower()
        if raw in {"q", "quit", "exit"}:
            print("Goodbye!")
            break
        try:
            age = int(raw)
        except ValueError:
            print("Please enter a whole number age or 'q' to quit.")
            continue
        print(get_person_category(age))
