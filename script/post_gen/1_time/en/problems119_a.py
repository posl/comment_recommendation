Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    year = int(s.split('/')[0])
    month = int(s.split('/')[1])
    day = int(s.split('/')[2])
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
Suggestion 2

def main():
    s = input()
    y = int(s.split('/')[0])
    m = int(s.split('/')[1])
    d = int(s.split('/')[2])
    if y < 2019:
        print('Heisei')
    elif y > 2019:
        print('TBD')
    elif y == 2019:
        if m < 4:
            print('Heisei')
        elif m > 4:
            print('TBD')
        elif m == 4:
            if d <= 30:
                print('Heisei')
            else:
                print('TBD')
    return

=======
Suggestion 3

def main():
    S = input()
    if S <= "2019/04/30":
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 4

def main():
    date = input()
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:])
    if year < 2019:
        print("Heisei")
    elif year == 2019:
        if month < 4:
            print("Heisei")
        elif month == 4:
            if day <= 30:
                print("Heisei")
            else:
                print("TBD")
        else:
            print("TBD")
    else:
        print("TBD")

=======
Suggestion 5

def main():
    date = input()
    if date <= "2019/04/30":
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 6

def main():
    s = input()
    year, month, day = s.split("/")
    year = int(year)
    month = int(month)
    day = int(day)
    if year < 2019:
        print("Heisei")
    elif year == 2019:
        if month <= 4:
            print("Heisei")
        else:
            print("TBD")
    else:
        print("TBD")

=======
Suggestion 7

def main():
    S = input()
    year = int(S[:4])
    month = int(S[5:7])
    day = int(S[-2:])

    if year < 2019:
        print("Heisei")
    elif year == 2019:
        if month <= 4:
            print("Heisei")
        else:
            print("TBD")
    else:
        print("TBD")

=======
Suggestion 8

def main():
    S = input().split('/')
    if int(S[0]) < 2019:
        print('Heisei')
    elif int(S[0]) > 2019:
        print('TBD')
    elif int(S[1]) < 4:
        print('Heisei')
    elif int(S[1]) > 4:
        print('TBD')
    elif int(S[2]) <= 30:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 9

def main():
    s = input()
    s = s.split('/')
    if int(s[0]) > 2019:
        print('TBD')
    elif int(s[0]) == 2019:
        if int(s[1]) > 4:
            print('TBD')
        elif int(s[1]) == 4:
            if int(s[2]) > 30:
                print('TBD')
            else:
                print('Heisei')
        else:
            print('Heisei')
    else:
        print('Heisei')

=======
Suggestion 10

def main():
    # Get input here
    s = input()

    # Calculate result here
    if s <= "2019/04/30":
        result = "Heisei"
    else:
        result = "TBD"

    # Print result here
    print(result)

main()
