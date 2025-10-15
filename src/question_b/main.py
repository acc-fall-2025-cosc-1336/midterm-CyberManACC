from question_b import is_prime

if __name__ == "__main__":
	while True:
		user_input = input("Enter a number to check if it's prime (or 'q' to quit): ")
		if user_input.lower() == 'q':
			print("Goodbye!")
			break
		try:
			num = int(user_input)
			print(f"is_prime({num}):", is_prime(num))
		except ValueError:
			print("Please enter a valid integer or 'q' to quit.")
#add import