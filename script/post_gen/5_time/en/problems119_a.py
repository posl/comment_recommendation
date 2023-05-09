Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # input
    S = input()

    # compute

    # output
    if S <= '2019/04/30':
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 2

def main():
    date = input()
    year = int(date.split("/")[0])
    month = int(date.split("/")[1])
    day = int(date.split("/")[2])
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
Suggestion 3

def main():
    S = input()
    year = int(S[0:4])
    month = int(S[5:7])
    day = int(S[8:10])
    if year < 2019:
        print("Heisei")
    elif year > 2019:
        print("TBD")
    else:
        if month < 4:
            print("Heisei")
        elif month > 4:
            print("TBD")
        else:
            if day <= 30:
                print("Heisei")
            else:
                print("TBD")

=======
Suggestion 4

def main():
    date = input()
    year = int(date.split('/')[0])
    month = int(date.split('/')[1])
    day = int(date.split('/')[2])
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
    s = input()
    if s <= '2019/04/30':
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 6

def main():
    date = input()
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:])
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
Suggestion 7

def main():
    S = input()
    if S <= '2019/04/30':
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 8

def main():
    s = input()
    y, m, d = s.split("/")
    y = int(y)
    m = int(m)
    d = int(d)

    if y < 2019:
        print("Heisei")
    elif y == 2019:
        if m < 4:
            print("Heisei")
        elif m == 4:
            if d <= 30:
                print("Heisei")
            else:
                print("TBD")
        else:
            print("TBD")
    else:
        print("TBD")

=======
Suggestion 9

def problems119_a():
    s = input()
    y, m, d = map(int, s.split('/'))
    if m <= 4:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 10

def main():
    S = input()
    print('Heisei') if int(S[5:7]) <= 4 else print('TBD')

main()
