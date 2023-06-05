Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    s = input()
    if s == "saturday" or s == "sunday":
        print(0)
    else:
        print(5-week.index(s))

=======
Suggestion 2

def main():
    day = input()
    week = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
    day_num = week.index(day)
    print(6 - day_num)

=======
Suggestion 3

def main():
    day = input()
    if day == '星期一':
        print(5)
    elif day == '星期二':
        print(4)
    elif day == '星期三':
        print(3)
    elif day == '星期四':
        print(2)
    elif day == '星期五':
        print(1)

=======
Suggestion 4

def get_days_to_saturday(s):
    days = 0
    if s == "星期一":
        days = 5
    elif s == "星期二":
        days = 4
    elif s == "星期三":
        days = 3
    elif s == "星期四":
        days = 2
    elif s == "星期五":
        days = 1
    return days

=======
Suggestion 5

def main():
    print("星期一")
    print("星期二")
    print("星期三")
    print("星期四")
    print("星期五")
    print("星期六")
    print("星期日")
    print("请输入:")
    a = input()
    if a == "星期一":
        print("5")
    elif a == "星期二":
        print("4")
    elif a == "星期三":
        print("3")
    elif a == "星期四":
        print("2")
    elif a == "星期五":
        print("1")
    elif a == "星期六":
        print("0")
    elif a == "星期日":
        print("6")

=======
Suggestion 6

def get_days_to_saturday(day):
    days = 0
    if day == 'Monday':
        days = 5
    if day == 'Tuesday':
        days = 4
    if day == 'Wednesday':
        days = 3
    if day == 'Thursday':
        days = 2
    if day == 'Friday':
        days = 1
    return days

=======
Suggestion 7

def main():
    day = input()
    day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    day_list = day_list[day_list.index(day):] + day_list[:day_list.index(day)]
    print(day_list.index('Saturday') + 1)

=======
Suggestion 8

def isWeekend(s):
    if s == '星期一':
        return 1
    elif s == '星期二':
        return 2
    elif s == '星期三':
        return 3
    elif s == '星期四':
        return 4
    elif s == '星期五':
        return 5
    elif s == '星期六':
        return 6
    elif s == '星期日':
        return 7

=======
Suggestion 9

def main():
    #读取输入
    s = input()
    #计算输出
    if s == '星期一':
        print(5)
    elif s == '星期二':
        print(4)
    elif s == '星期三':
        print(3)
    elif s == '星期四':
        print(2)
    elif s == '星期五':
        print(1)

=======
Suggestion 10

def main():
    week = input()

    if week == '星期一':
        print(5)
    elif week == '星期二':
        print(4)
    elif week == '星期三':
        print(3)
    elif week == '星期四':
        print(2)
    elif week == '星期五':
        print(1)
