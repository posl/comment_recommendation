def main():
    # Read the input
    s = input()
    # Create a dictionary with the days of the week
    days = {'SUN': 7, 'MON': 6, 'TUE': 5, 'WED': 4, 'THU': 3, 'FRI': 2, 'SAT': 1}
    # Print the number of days before the next Sunday
    print(days[s])

if __name__ == '__main__':
    main()