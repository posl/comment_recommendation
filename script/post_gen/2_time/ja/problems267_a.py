Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s == "Monday":
        print(5)
    elif s == "Tuesday":
        print(4)
    elif s == "Wednesday":
        print(3)
    elif s == "Thursday":
        print(2)
    elif s == "Friday":
        print(1)
    else:
        print(0)

=======
Suggestion 2

def solve():
    s = input()
    if s == "Monday":
        print(5)
    elif s == "Tuesday":
        print(4)
    elif s == "Wednesday":
        print(3)
    elif s == "Thursday":
        print(2)
    elif s == "Friday":
        print(1)
    elif s == "Saturday":
        print(0)
    else:
        print(6)

=======
Suggestion 3

def main():
    s = input()
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    print(5 - week.index(s))

=======
Suggestion 4

def main():
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    s = input()
    print(5 - week.index(s))

=======
Suggestion 5

def solve():
    s = input()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i, day in enumerate(days):
        if s == day:
            print(6 - i)

=======
Suggestion 6

def main():
    s = input()
    day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    day_count = 0
    for i in range(len(day)):
        if s == day[i]:
            day_count = i
    print(5 - day_count)

=======
Suggestion 7

def main():
    day = input()
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    print(5 - week.index(day))

=======
Suggestion 8

def get_days(day):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return 7 - days.index(day)

=======
Suggestion 9

def main():
    week = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    s = input()
    print(5-week.index(s))

=======
Suggestion 10

def get_days(week):
    week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return week_list.index(week) + 1
