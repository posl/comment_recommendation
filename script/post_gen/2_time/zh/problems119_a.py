Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S <= '2019/04/30':
        print('平成')
    else:
        print('TBD')

=======
Suggestion 2

def main():
    date = input()
    if date <= "2019/04/30":
        print("平成")
    else:
        print("TBD")

=======
Suggestion 3

def main():
    s = input()
    y, m, d = map(int, s.split('/'))
    if (y < 2019):
        print('Heisei')
    elif (y == 2019 and m <= 4):
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 4

def main():
    s = input()
    year, month, day = map(int, s.split('/'))
    if year < 2019:
        print('Heisei')
    elif year == 2019:
        if month <= 4:
            print('Heisei')
        else:
            print('TBD')
    else:
        print('TBD')

=======
Suggestion 5

def main():
    s = input()
    year, month, day = map(int, s.split('/'))
    if year < 2019:
        print("Heisei")
        return
    if year == 2019 and month <= 4:
        print("Heisei")
        return
    print("TBD")

=======
Suggestion 6

def main():
    date = list(map(int, input().split('/')))
    if date[0] < 2019:
        print('Heisei')
    elif date[1] < 4:
        print('Heisei')
    elif date[2] <= 30:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 7

def main():
    s=input()
    year=int(s[:4])
    month=int(s[5:7])
    day=int(s[8:])
    if year<2019:
        print("Heisei")
    elif year==2019:
        if month<=4:
            print("Heisei")
        else:
            print("TBD")
    else:
        print("TBD")

=======
Suggestion 8

def main():
    s = input()
    if s <= "2019/04/30":
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 9

def main():
    s = input()
    year, month, day = map(int, s.split('/'))
    if year < 2019:
        print('Heisei')
    elif year > 2019:
        print('TBD')
    elif month < 4:
        print('Heisei')
    elif month > 4:
        print('TBD')
    elif day <= 30:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 10

def main():
    # 输入
    S = input()
    #分割字符串
    S = S.split('/')
    # 年月日
    year = int(S[0])
    month = int(S[1])
    day = int(S[2])
    # 判断
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
