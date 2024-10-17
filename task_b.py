try:
    # Get input from the user and try to convert it to an integer
    grade = int(input("Enter a numerical grade (0-100): "))

    # Check if the grade is within the valid range of 0 to 100
    if 0 <= grade <= 100:
        if 80 <= grade <= 100:
            letter = "A"
        elif 60 <= grade <= 79:
            letter = "B"
        elif 50 <= grade <= 59:
            letter = "C"
        elif 40 <= grade <= 49:
            letter = "D"
        else:
            letter = "F"
        # Print the corresponding letter grade
        print(f"Your grade is: {letter}")
    else:
        # If the grade is outside the valid range of 0 to 100
        print("Error: Grades must be between 0 and 100")

except ValueError:
    # If the input is not a valid number
    print("Error: Please enter a number")
 