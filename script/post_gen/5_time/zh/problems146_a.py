Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    print(7-week.index(input()))

=======
Suggestion 2

def main():
    s = input()
    if s == "SUN":
        print(7)
    elif s == "MON":
        print(6)
    elif s == "TUE":
        print(5)
    elif s == "WED":
        print(4)
    elif s == "THU":
        print(3)
    elif s == "FRI":
        print(2)
    elif s == "SAT":
        print(1)
    else:
        print("error")

=======
Suggestion 3

def get_day(day):
    if day == 'SUN':
        return 0
    elif day == 'MON':
        return 1
    elif day == 'TUE':
        return 2
    elif day == 'WED':
        return 3
    elif day == 'THU':
        return 4
    elif day == 'FRI':
        return 5
    elif day == 'SAT':
        return 6

=======
Suggestion 4

def main():
    s = input()
    day = 0
    if s == 'SUN':
        day = 7
    elif s == 'MON':
        day = 6
    elif s == 'TUE':
        day = 5
    elif s == 'WED':
        day = 4
    elif s == 'THU':
        day = 3
    elif s == 'FRI':
        day = 2
    elif s == 'SAT':
        day = 1
    print(day)

=======
Suggestion 5

def solve():
    s = input()
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    print(7 - days.index(s))

=======
Suggestion 6

def get_next_date(day):
    if day == 'SUN':
        return 7
    elif day == 'MON':
        return 6
    elif day == 'TUE':
        return 5
    elif day == 'WED':
        return 4
    elif day == 'THU':
        return 3
    elif day == 'FRI':
        return 2
    elif day == 'SAT':
        return 1

=======
Suggestion 7

def main():
    week = input()
    week_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(7 - week_list.index(week))

=======
Suggestion 8

def main():
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    day = 7
    s = input()
    print(day - week.index(s))

=======
Suggestion 9

def problem146a(s):
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    return 7 - week.index(s)

=======
Suggestion 10

def main():
    week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    s = input()
    print(7 - week.index(s))
