Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S <= '2019/04/30':
        print('Heisei')
    else:
        print('TBD')

main()

=======
Suggestion 2

def main():
    date = input()
    if date <= "2019/04/30":
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 3

def main():
    date = input()
    if date <= '2019/04/30':
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 4

def main():
    S = input()
    year = int(S[0:4])
    month = int(S[5:7])
    day = int(S[8:10])
    if year < 2019:
        print('Heisei')
    elif year == 2019:
        if month < 4:
            print('Heisei')
        elif month == 4:
            if day <= 30:
                print('Heisei')
            else:
                print('TBD')
        else:
            print('TBD')
    else:
        print('TBD')

=======
Suggestion 5

def main():
    date = input()
    y, m, d = date.split('/')
    if int(y) < 2019:
        print("Heisei")
    elif int(y) == 2019:
        if int(m) < 5:
            print("Heisei")
        elif int(m) == 4:
            if int(d) < 31:
                print("Heisei")
            else:
                print("TBD")
        else:
            print("TBD")
    else:
        print("TBD")

=======
Suggestion 6

def main():
    S = input()
    S = S.split("/")

    if int(S[0]) < 2019:
        print("Heisei")
    elif int(S[0]) == 2019 and int(S[1]) < 5:
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 7

def main():
    date = input()
    #print(date)
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    #print(year)
    #print(month)
    #print(day)
    if year <= 2019:
        if month <= 4:
            print("Heisei")
        else:
            print("TBD")
    else:
        print("TBD")

=======
Suggestion 8

def main():
    s = input()
    print("Heisei" if s < "2019/04/30" else "TBD")

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    #Get input
    inp = input()
    #Split input into array
    inp = inp.split("/")
    #Check if month is less than 4
    if int(inp[1]) < 4:
        print("Heisei")
    #Check if month is 4 and day is less than 30
    elif int(inp[1]) == 4 and int(inp[2]) < 30:
        print("Heisei")
    #Otherwise print TBD
    else:
        print("TBD")
