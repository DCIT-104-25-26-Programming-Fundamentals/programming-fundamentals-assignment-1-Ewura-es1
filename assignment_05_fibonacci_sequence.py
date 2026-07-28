# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================

# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
def print_fibonacci(n):
    """
    Generates and prints the first N terms of the Fibonacci sequence.
    """
    if n <= 0:
        print("Error: Please enter a positive integer greater than 0.")
        return

    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    print("Fibonacci sequence:", " ".join(map(str, sequence)))


# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
def is_fibonacci(num):
    """
    Checks whether a given non-negative integer belongs to the Fibonacci sequence.
    Returns True if it is a Fibonacci number, False otherwise.
    """
    if num < 0:
        return False

    a, b = 0, 1
    while a < num:
        a, b = b, a + b

    return a == num


# =============================================================================
# MAIN PROGRAM
# =============================================================================
def main():
    # --- PART A ---
    print("=== PART A: PRINT FIRST N TERMS ===")
    try:
        n_terms = int(input("How many terms? "))
        print_fibonacci(n_terms)
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

    print("\n" + "-" * 40 + "\n")

    # --- PART B ---
    print("=== PART B: CHECK FIBONACCI NUMBER ===")
    try:
        target = int(input("Enter a number to check: "))
        if target < 0:
            print("Error: Please enter a non-negative integer.")
        elif is_fibonacci(target):
            print(f"{target} is a Fibonacci number.")
        else:
            print(f"{target} is NOT a Fibonacci number.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()