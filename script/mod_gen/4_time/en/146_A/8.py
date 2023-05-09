def main():
    # Get the day of the week
    day = input()
    # Create a list of the days of the week
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    # Print the number of days until the next Sunday
    print(7 - days.index(day))

if __name__ == '__main__':
    main()