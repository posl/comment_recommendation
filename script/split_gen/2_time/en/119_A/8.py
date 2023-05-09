def main():
    # Read the date
    date = input()
    # Split the date into a list
    date = date.split("/")
    # Check if the month is greater than 4
    if int(date[1]) > 4:
        # Print TBD
        print("TBD")
    # Check if the month is 4 and the day is greater than 30
    elif int(date[1]) == 4 and int(date[2]) > 30:
        # Print TBD
        print("TBD")
    # If the month is 4 and the day is not greater than 30
    else:
        # Print Heisei
        print("Heisei")
