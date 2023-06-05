Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # input
    s = input()
    # check
    if s <= '2019/04/30':
        print('平成')
    else:
        print('TBD')

=======
Suggestion 2

def main():
    date = input()
    year = int(date.split('/')[0])
    month = int(date.split('/')[1])
    day = int(date.split('/')[2])
    if year < 2019:
        print('Heisei')
    elif year == 2019 and month <= 4 and day <= 30:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 3

def main():
    # 输入
    s = input()
    # 处理
    # 切分字符串
    s_list = s.split('/')
    # 判断
    if int(s_list[0]) < 2019:
        print('Heisei')
    elif int(s_list[0]) == 2019:
        if int(s_list[1]) < 4:
            print('Heisei')
        elif int(s_list[1]) == 4:
            if int(s_list[2]) <= 30:
                print('Heisei')
            else:
                print('TBD')
        else:
            print('TBD')
    else:
        print('TBD')
    # 输出

=======
Suggestion 4

def main():
    str = input()
    str = str.replace("/","")
    if int(str) <= 20190430:
        print("平成")
    else:
        print("TBD")

=======
Suggestion 5

def main():
    S = input()
    year, month, day = S.split('/')
    if int(year) < 2019:
        print('Heisei')
    elif int(year) == 2019:
        if int(month) < 4:
            print('Heisei')
        elif int(month) == 4:
            if int(day) <= 30:
                print('Heisei')
            else:
                print('TBD')
        else:
            print('TBD')
    else:
        print('TBD')

=======
Suggestion 6

def problem119_a():
    s = input()
    s1 = s.split('/')
    if int(s1[1]) < 5:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 7

def get_year(s):
    return int(s.split('/')[0])

=======
Suggestion 8

def main():
    input_date = input()
    year, month, day = input_date.split('/')
    if int(year) < 2019:
        print('Heisei')
    elif int(year) == 2019 and int(month) <= 4:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 9

def main():
    s = input()
    if s <= "2019/04/30":
        print("平成")
    else:
        print("TBD")

=======
Suggestion 10

def main():
    date = input()
    year = int(date.split('/')[0])
    month = int(date.split('/')[1])
    day = int(date.split('/')[2])
    if year < 2019:
        print('Heisei')
    elif year > 2019:
        print('TBD')
    else:
        if month <= 4:
            print('Heisei')
        else:
            print('TBD')
