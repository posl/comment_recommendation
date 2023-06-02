Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    y,m,d = S.split('/')
    if int(y)<2019:
        print('Heisei')
    elif int(m)<4:
        print('Heisei')
    elif int(d)<=30:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 2

def main():
    S = input()
    if S <= "2019/04/30":
        print("平成")
    else:
        print("TBD")

=======
Suggestion 3

def main():
    # 读入数据
    str = input()
    # 处理数据
    # 切分字符串
    year, month, day = str.split("/")
    # 判断是否小于等于2019/04/30
    if year < "2019" or (year == "2019" and month < "04") or (year == "2019" and month == "04" and day <= "30"):
        print("平成")
    else:
        print("TBD")

=======
Suggestion 4

def main():
    import datetime
    s = input()
    y = int(s[:4])
    m = int(s[5:7])
    d = int(s[8:])
    if datetime.date(y, m, d) <= datetime.date(2019, 4, 30):
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 5

def main():
    date = input()
    year, month, day = date.split('/')
    if int(year) < 2019:
        print('Heisei')
    elif int(year) == 2019 and int(month) <= 4 and int(day) <= 30:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 6

def main():
    S = input()
    S = S.split('/')
    if int(S[0]) < 2019:
        print('Heisei')
    elif int(S[1]) < 5:
        print('Heisei')
    elif int(S[2]) <= 30:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 7

def problem119_a():
    input_str = input()
    year = int(input_str[0:4])
    month = int(input_str[5:7])
    day = int(input_str[8:10])
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
Suggestion 8

def judge(s):
    if s <= "2019/04/30":
        print("平成")
    else:
        print("TBD")

=======
Suggestion 9

def main():
    date = input().split('/')
    if int(date[1]) > 4:
        print('TBD')
    else:
        print('Heisei')

main()

=======
Suggestion 10

def main():
    date = input()
    # print(date)
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:])
    # print(year,month,day)
    if year < 2019:
        print('Heisei')
    elif year == 2019 and month <= 4 and day <= 30:
        print('Heisei')
    else:
        print('TBD')
