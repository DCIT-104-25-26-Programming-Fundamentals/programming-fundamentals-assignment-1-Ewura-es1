# Ask for input
user_input = input("Enter student score (0-100): ")
score = int(user_input)

# Check the score directly
if score < 0 or score > 100:
    print("Error: Score must be between 0 and 100.")
elif score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
else:
    print("Grade: F")
