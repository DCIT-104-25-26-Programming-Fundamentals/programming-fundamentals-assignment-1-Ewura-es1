<<<<<<< HEAD
def compute_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def compute_average(numbers):
    if len(numbers) == 0:
        return 0
    return compute_sum(numbers) / len(numbers)

def compute_max(numbers):
    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
    return highest

def compute_min(numbers):
    lowest = numbers[0]
    for num in numbers:
        if num < lowest:
            lowest = num
    return lowest

def main():

    user_input = input("How many numbers? ")
    n = int(user_input)
    
    
    if n <= 0:
        print("Error: Number of items must be greater than 0.")
        return

    numbers = []
    
    
    for i in range(n):
        num_input = input(f"Enter number {i + 1}: ")
        numbers.append(float(num_input))
        
    # Print the calculated statistical values
    print("\nResults:")
    print(f"Sum: {compute_sum(numbers)}")
    print(f"Average: {compute_average(numbers)}")
    print(f"Maximum: {compute_max(numbers)}")
    print(f"Minimum: {compute_min(numbers)}")

if __name__ == "__main__":
    main()
=======
# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

>>>>>>> a77fe08d75f33674bbcbcc02ddae006df6b1ace0
