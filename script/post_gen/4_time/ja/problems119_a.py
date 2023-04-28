Synthesizing 7/10 solutions

=======
Suggestion 1

def main():
    s = input()
    y = int(s[0:4])
    m = int(s[5:7])
    d = int(s[8:10])
    if y < 2019:
        print("Heisei")
    elif y == 2019 and m <= 4 and d <= 30:
        print("Heisei")
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

def judge(year, month, day):
    if year > 2019:
        return "TBD"
    elif year < 2019:
        return "Heisei"
    elif month > 4:
        return "TBD"
    elif month < 4:
        return "Heisei"
    elif day > 30:
        return "TBD"
    else:
        return "Heisei"

year, month, day = map(int, input().split("/"))
print(judge(year, month, day))

=======
Suggestion 4

def main():
    S = input()
    y, m, d = S.split('/')
    y = int(y)
    m = int(m)
    d = int(d)
    if y < 2019:
        print('Heisei')
    elif y == 2019:
        if m < 4:
            print('Heisei')
        elif m == 4:
            if d <= 30:
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
    y, m, d = map(int, s.split("/"))
    if y < 2019:
        print("Heisei")
    elif y == 2019 and m < 4:
        print("Heisei")
    elif y == 2019 and m == 4 and d <= 30:
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 6

def judge():
    s = input()
    s = s.split('/')

    if int(s[0]) > 2019:
        print('TBD')
    elif int(s[1]) > 4:
        print('TBD')
    elif int(s[2]) > 30:
        print('TBD')
    else:
        print('Heisei')

judge()

=======
Suggestion 7

def main():
    s = input()
    s = s.replace('/','')
    if int(s) >= 20190430:
        print('TBD')
    else:
        print('Heisei')
