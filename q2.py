def leapYear(value):
    if (int(value) % 4 == 0):
        if (int(value) % 100 == 0):
            return "This is not a leap year."
        else:
            return "This is a leap year."
    else:
        print("This is not a leap year.")
