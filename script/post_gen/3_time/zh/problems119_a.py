Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
  # input
  s = input()
  # output
  if s <= "2019/04/30":
    print("平成")
  else:
    print("TBD")

=======
Suggestion 2

def main():
    date = input()
    if date <= '2019/04/30':
        print("平成")
    else:
        print("TBD")

=======
Suggestion 3

def main():
    date = input()
    date_list = date.split('/')
    if int(date_list[0]) < 2019:
        print('Heisei')
    elif int(date_list[0]) == 2019:
        if int(date_list[1]) < 4:
            print('Heisei')
        elif int(date_list[1]) == 4:
            if int(date_list[2]) <= 30:
                print('Heisei')
            else:
                print('TBD')
        else:
            print('TBD')
    else:
        print('TBD')

=======
Suggestion 4

def main():
    # 读取输入
    S = input()

    # 请在下面编写你的代码
    year, month, day = S.split('/')
    year = int(year)
    month = int(month)
    day = int(day)
    if year < 2019:
        print('平成')
    elif year == 2019:
        if month < 4:
            print('平成')
        elif month == 4:
            if day <= 30:
                print('平成')
            else:
                print('TBD')
        else:
            print('TBD')
    else:
        print('TBD')

=======
Suggestion 5

def main():
    S = input()
    if S <= '2019/04/30':
        print('平成')
    else:
        print('TBD')

=======
Suggestion 6

def main():
    date = input()
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])

    if year < 2019:
        print("Heisei")
    elif year == 2019 and month < 4:
        print("Heisei")
    elif year == 2019 and month == 4 and day <= 30:
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 7

def main():
    s = input()
    ymd = s.split("/")
    if int(ymd[0]) < 2019:
        print("Heisei")
    elif int(ymd[0]) == 2019 and int(ymd[1]) < 4:
        print("Heisei")
    elif int(ymd[0]) == 2019 and int(ymd[1]) == 4 and int(ymd[2]) <= 30:
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 8

def problem119_a():
    s = input()
    if s <= '2019/04/30':
        print('Heisei')
    else:
        print('TBD')
problem119_a()

=======
Suggestion 9

def main():
    S = input()
    year = int(S[0:4])
    month = int(S[5:7])
    day = int(S[8:])
    if year < 2019:
        print("Heisei")
    elif year > 2019:
        print("TBD")
    elif month < 4:
        print("Heisei")
    elif month > 4:
        print("TBD")
    elif day <= 30:
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 10

def main():
    s = input()
    s = s.split('/')
    if int(s[0]) < 2019:
        print('Heisei')
    elif int(s[0]) == 2019:
        if int(s[1]) < 4:
            print('Heisei')
        elif int(s[1]) == 4:
            if int(s[2]) <= 30:
                print('Heisei')
            else:
                print('TBD')
        else:
            print('TBD')
    else:
        print('TBD')
