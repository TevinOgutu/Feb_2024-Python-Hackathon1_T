def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize the sequence with the first two terms

    # Generate Fibonacci sequence up to term n
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

def main():
    # Ask the user to input the value of n
    n = int(input("Enter the number of terms in the Fibonacci sequence: "))

    # Check if n is valid
    if n <= 0:
        print("Please enter a positive integer.")
        return

    # Generate Fibonacci sequence
    fibonacci_sequence = generate_fibonacci(n)

    # Print the generated Fibonacci sequence
    print("Fibonacci sequence up to term", n, ":")
    print(fibonacci_sequence)

if __name__ == "__main__":
    main()
