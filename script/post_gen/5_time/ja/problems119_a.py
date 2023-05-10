Synthesizing 9/10 solutions

=======
Suggestion 1

def judgeHeisei(date):
    if date <= 430:
        return "Heisei"
    else:
        return "TBD"

=======
Suggestion 2

def main():
    s = input()
    s = s.split("/")
    if int(s[0]) < 2019:
        print("Heisei")
    elif int(s[0]) == 2019:
        if int(s[1]) < 5:
            print("Heisei")
        elif int(s[1]) == 5:
            if int(s[2]) <= 30:
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
    S_list = S.split("/")
    S_year = int(S_list[0])
    S_month = int(S_list[1])
    S_day = int(S_list[2])

    if S_year < 2019:
        print("Heisei")
    elif S_year == 2019:
        if S_month < 4:
            print("Heisei")
        elif S_month == 4:
            if S_day <= 30:
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
    y, m, d = s.split('/')
    y = int(y)
    m = int(m)
    d = int(d)
    if y < 2019:
        print('Heisei')
    elif y == 2019 and m <= 4:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 5

def main():
    s = input()
    year, month, day = s.split('/')
    if int(year) < 2019:
        print('Heisei')
    elif int(year) > 2019:
        print('TBD')
    else:
        if int(month) < 4:
            print('Heisei')
        elif int(month) > 4:
            print('TBD')
        else:
            if int(day) <= 30:
                print('Heisei')
            else:
                print('TBD')

=======
Suggestion 6

def judge(s):
    if s <= "2019/04/30":
        print("Heisei")
    else:
        print("TBD")

s = input()
judge(s)

=======
Suggestion 7

def main():
    s = input()
    y, m, d = map(int, s.split('/'))
    if y < 2019:
        print('Heisei')
    elif y == 2019 and m <= 4:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 8

def main():
    s = input()
    y = int(s[:4])
    m = int(s[5:7])
    d = int(s[8:10])
    if y < 2019:
        print("Heisei")
    elif y == 2019 and m < 4:
        print("Heisei")
    elif y == 2019 and m == 4 and d <= 30:
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 9

def judge():
    s = input()
    if s <= "2019/04/30":
        print("Heisei")
    else:
        print("TBD")
