
days_of_week = {
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6,
    "sunday": 7
}

day = input("Enter a day of the week: ").strip().lower()

if day in days_of_week:
    day_number = days_of_week[day]
    formatted_day = day.capitalize()
    print(f"{formatted_day} is day {day_number}")
else:
    print("Please enter a valid day")

