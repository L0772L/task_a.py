grade = int(input("Enter a numerical grade (0-100): "))

if 80 <= grade <= 100:
    letter = "A"
elif 60 <= grade <= 79:
    letter = "B"
elif 50 <= grade <= 59:
    letter = "C"
elif 40 <= grade <= 49:
    letter = "D"
elif 0 <= grade <= 39:
    letter = "F"
else:
    letter = "Invalid"

if letter == "Invalid":
    print("Please enter a valid grade between 0 and 100.")
else:
    print(f"The grade is: {letter}")
 