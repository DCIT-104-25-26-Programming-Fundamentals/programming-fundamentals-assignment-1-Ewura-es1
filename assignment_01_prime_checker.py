def is_prime(number):
    # Numbers less than 2 are not prime
    if number < 2:
        return False
        
    # Check for factors from 2 up to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # Found a divisor, so it is not prime
            
    return True  # No divisors found, it is prime

def main():
    # Get input from the user
    user_input = int(input("Enter a number: "))
    
    # Call the function and print the result
    if is_prime(user_input):
        print(f"{user_input} is a prime number.")
    else:
        print(f"{user_input} is NOT a prime number.")

# Run the main function
if __name__ == "__main__":
    main()
