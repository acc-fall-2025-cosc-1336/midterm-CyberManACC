def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    # check divisors of the form 6k ± 1 up to sqrt(n)
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    # 3) Interactive program: prompt until user decides to quit
    print("Prime checker (type 'q' to quit)")
    while True:
        s = input("Enter an integer (or 'q' to quit): ").strip().lower()
        if s in {"q", "quit", "exit"}:
            print("Goodbye!")
            break
        try:
            val = int(s)
        except ValueError:
            print("Please enter a valid integer or 'q' to quit.")
            continue
        print(f"{val} is {'prime' if is_prime(val) else 'not prime'}")

