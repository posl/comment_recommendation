Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    week = ['星期一','星期二','星期三','星期四','星期五','星期六','星期天']
    day = input()
    day = week.index(day)
    print(5-day)

=======
Suggestion 2

def get_days_to_saturday(day):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return 7 - days.index(day) if days.index(day) < 5 else 0

=======
Suggestion 3

def main():
    # 读取输入
    s = input()
    # 处理
    if s == "星期一":
        print(5)
    elif s == "星期二":
        print(4)
    elif s == "星期三":
        print(3)
    elif s == "星期四":
        print(2)
    else:
        print(1)

=======
Suggestion 4

def main():
    week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    s = input()
    print(6-week.index(s))

=======
Suggestion 5

def get_days_of_week(week_day):
    week_days = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
    return week_days.index(week_day)+1

=======
Suggestion 6

def main():
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    s = input()
    print(7 - days.index(s))

=======
Suggestion 7

def main():
    day = input()
    if day == "星期一":
        print(5)
    elif day == "星期二":
        print(4)
    elif day == "星期三":
        print(3)
    elif day == "星期四":
        print(2)
    elif day == "星期五":
        print(1)
    else:
        print(0)

=======
Suggestion 8

def main():
    day = input()
    if day == "星期一":
        print(5)
    elif day == "星期二":
        print(4)
    elif day == "星期三":
        print(3)
    elif day == "星期四":
        print(2)
    elif day == "星期五":
        print(1)
    else:
        pass

=======
Suggestion 9

def main():
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    s = input()
    print(week.index('SAT') - week.index(s))

=======
Suggestion 10

def main():
    week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    S = input()
    print(week.index('Saturday') - week.index(S))
