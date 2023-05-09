def main():
    # Read the input
    S = input()
    
    # Convert the string to integer
    S = S.upper()
    if S == "SUN":
        S = 0
    elif S == "MON":
        S = 1
    elif S == "TUE":
        S = 2
    elif S == "WED":
        S = 3
    elif S == "THU":
        S = 4
    elif S == "FRI":
        S = 5
    elif S == "SAT":
        S = 6
    
    # Calculate the number of days to Sunday
    days = 7 - S
    
    # Print the result
    print(days)

if __name__ == '__main__':
    main()