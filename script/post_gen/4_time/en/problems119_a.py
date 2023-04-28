Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    y = int(s[0:4])
    m = int(s[5:7])
    d = int(s[8:10])
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
Suggestion 2

def main():
    s = input()
    year = int(s[0:4])
    month = int(s[5:7])
    day = int(s[8:10])
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
    s = input()
    year = int(s.split("/")[0])
    month = int(s.split("/")[1])
    day = int(s.split("/")[2])
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
Suggestion 4

def main():
    s = input()
    y = int(s[0:4])
    m = int(s[5:7])
    d = int(s[8:10])
    if y < 2019:
        print('Heisei')
    elif y > 2019:
        print('TBD')
    else:
        if m < 4:
            print('Heisei')
        elif m > 4:
            print('TBD')
        else:
            if d <= 30:
                print('Heisei')
            else:
                print('TBD')

=======
Suggestion 5

def main():
    S = input()
    year, month, day = S.split('/')
    year = int(year)
    month = int(month)
    day = int(day)
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
Suggestion 6

def main():
    S = input()
    y, m, d = map(int, S.split('/'))
    if m <= 4:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 7

def main():
    s = input()
    y, m, d = s.split('/')
    if int(y) < 2019:
        print('Heisei')
    elif int(y) == 2019:
        if int(m) < 4:
            print('Heisei')
        elif int(m) == 4:
            if int(d) <= 30:
                print('Heisei')
            else:
                print('TBD')
        else:
            print('TBD')
    else:
        print('TBD')

=======
Suggestion 8

def main():
    S = input()
    year, month, day = S.split('/')
    if int(year) < 2019:
        print("Heisei")
    elif int(year) == 2019:
        if int(month) < 5:
            print("Heisei")
        elif int(month) == 5 and int(day) <= 31:
            print("Heisei")
        else:
            print("TBD")
    else:
        print("TBD")

=======
Suggestion 9

def main():
    S = input()
    S = S.split('/')
    if int(S[1]) <= 4:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 10

def is_heisei(s):
    if s <= '2019/04/30':
        return 'Heisei'
    else:
        return 'TBD'
