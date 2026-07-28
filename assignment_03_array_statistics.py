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
