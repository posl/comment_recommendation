Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s == 'Monday':
        print(5)
    elif s == 'Tuesday':
        print(4)
    elif s == 'Wednesday':
        print(3)
    elif s == 'Thursday':
        print(2)
    elif s == 'Friday':
        print(1)
    else:
        print(0)

=======
Suggestion 2

def day_to_int(day):
    if day == "Monday":
        return 0
    elif day == "Tuesday":
        return 1
    elif day == "Wednesday":
        return 2
    elif day == "Thursday":
        return 3
    elif day == "Friday":
        return 4
    elif day == "Saturday":
        return 5
    elif day == "Sunday":
        return 6

=======
Suggestion 3

def calc_days(s):
    days = 0
    if s == "Monday":
        days = 5
    elif s == "Tuesday":
        days = 4
    elif s == "Wednesday":
        days = 3
    elif s == "Thursday":
        days = 2
    elif s == "Friday":
        days = 1
    return days

=======
Suggestion 4

def main():
    s = input()
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    for i in range(5):
        if s == week[i]:
            print(5 - i)
            exit()

=======
Suggestion 5

def main():
    S = input()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    for i in range(5):
        if S == days[i]:
            print(5 - i)
            break

=======
Suggestion 6

def main():
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    s = input()
    print(5 - week.index(s))

=======
Suggestion 7

def main():
    s = input()
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print(5 - week.index(s))

=======
Suggestion 8

def get_days(s):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days.index("Saturday") - days.index(s)

print(get_days(input()))

=======
Suggestion 9

def get_weekday_index(weekday):
    weekday_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return weekday_list.index(weekday)

=======
Suggestion 10

def main():
    day = input()
    week = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
    print(week.index("Saturday") - week.index(day))
