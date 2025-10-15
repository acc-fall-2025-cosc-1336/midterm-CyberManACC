def get_person_category(age: int) -> str:
    """
    Return the category for a given age:
    - age < 0 or age > 125 -> "Invalid number"
    - 0 <= age <= 1        -> "infant"
    - 2 <= age <= 12       -> "child"
    - 13 <= age <= 19      -> "teenager"
    - age >= 20            -> "adult"
    """
    if age < 0 or age > 125:
        return "Invalid number"
    if age <= 1:
        return "infant"
    if age < 13:
        return "child"
    if age < 20:
        return "teenager"
    return "adult"


if __name__ == "__main__":
    # 3) Run until user quits
    print("Age category checker (type 'q' to quit)")
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

