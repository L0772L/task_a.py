try:
    grade = int(input("Enter a numerical grade (0-100): "))

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
        print(f"Your grade is: {letter}")
    else:
        print("Error: Grades must be between 0 and 100")

except ValueError:
    print("Error: Please enter a number")
 