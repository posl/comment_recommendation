Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    day = input()
    if day == '星期日':
        print(0)
    elif day == '星期一':
        print(5)
    elif day == '星期二':
        print(4)
    elif day == '星期三':
        print(3)
    elif day == '星期四':
        print(2)
    elif day == '星期五':
        print(1)
    elif day == '星期六':
        print(0)

=======
Suggestion 2

def main():
    weekday = input()
    weekday = weekday.upper()
    if weekday == 'MONDAY':
        print(5)
    elif weekday == 'TUESDAY':
        print(4)
    elif weekday == 'WEDNESDAY':
        print(3)
    elif weekday == 'THURSDAY':
        print(2)
    elif weekday == 'FRIDAY':
        print(1)
    else:
        print(0)

=======
Suggestion 3

def main():
    day = input()
    day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print(5 - day_list.index(day))

=======
Suggestion 4

def main():
    day = input()
    days = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    print(7 - days.index(day))

=======
Suggestion 5

def get_day_num(day):
    day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_num = day_list.index(day)
    return 7 - day_num

=======
Suggestion 6

def get_days_to_sat(s):
    days_to_sat = 0
    if s == '星期一':
        days_to_sat = 5
    elif s == '星期二':
        days_to_sat = 4
    elif s == '星期三':
        days_to_sat = 3
    elif s == '星期四':
        days_to_sat = 2
    elif s == '星期五':
        days_to_sat = 1
    return days_to_sat

=======
Suggestion 7

def main():
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    s = input()
    index = week.index(s)
    print(6-index)

=======
Suggestion 8

def main():
    week = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
    s = input()
    for i in range(7):
        if s == week[i]:
            break
    print(7-i)

=======
Suggestion 9

def get_days(s):
    days = 0
    for i in range(6):
        if s == 'Saturday':
            break
        elif s == 'Friday':
            days += 1
            s = 'Saturday'
        elif s == 'Thursday':
            days += 2
            s = 'Saturday'
        elif s == 'Wednesday':
            days += 3
            s = 'Saturday'
        elif s == 'Tuesday':
            days += 4
            s = 'Saturday'
        elif s == 'Monday':
            days += 5
            s = 'Saturday'
    return days

=======
Suggestion 10

def get_days_to_saturday(day):
    days = {"星期一":5, "星期二":4, "星期三":3, "星期四":2, "星期五":1}
    return days[day]
