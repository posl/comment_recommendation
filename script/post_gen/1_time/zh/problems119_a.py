Synthesizing 10/10 solutions

=======
Suggestion 1

def chenggong():
    print("平成")

=======
Suggestion 2

def problem119_a():
    S = input()
    S = S.split("/")
    if int(S[0]) < 2019:
        print("Heisei")
    elif int(S[0]) == 2019:
        if int(S[1]) < 4:
            print("Heisei")
        elif int(S[1]) == 4:
            if int(S[2]) <= 30:
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
    year, month, day = S.split('/')
    year = int(year)
    month = int(month)
    day = int(day)
    if year < 2019:
        print('Heisei')
    elif year == 2019 and month <= 4:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 4

def main():
    #input
    date = input()
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    #compute
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
main()

=======
Suggestion 5

def main():
    S = input()
    y = int(S[0:4])
    m = int(S[5:7])
    d = int(S[8:10])
    if y < 2019:
        print("Heisei")
    elif y == 2019 and m <= 4:
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 6

def main():
    # 日期输入
    date = input()
    # 年月日分离
    year, month, day = date.split('/')
    # 判断
    if int(year) < 2019:
        print('Heisei')
    elif int(year) == 2019 and int(month) < 4:
        print('Heisei')
    elif int(year) == 2019 and int(month) == 4 and int(day) <= 30:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 7

def main():
    str = input()
    str_list = str.split('/')
    if int(str_list[0]) < 2019:
        print('Heisei')
    elif int(str_list[1]) < 4:
        print('Heisei')
    elif int(str_list[2]) <= 30:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 8

def main():
    S = input()
    if S <= "2019/04/30":
        print("平成")
    else:
        print("TBD")

=======
Suggestion 9

def main():
    S = input()
    year, month, day = S.split('/')
    year = int(year)
    month = int(month)
    day = int(day)
    if year < 2019:
        print('Heisei')
    elif year == 2019 and month < 4:
        print('Heisei')
    elif year == 2019 and month == 4 and day <= 30:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 10

def get_input():
    return input()
