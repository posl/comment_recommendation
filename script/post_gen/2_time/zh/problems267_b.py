Synthesizing 10/10 solutions

=======
Suggestion 1

def get_weekday(weekday):
    weekdays = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    return weekdays.index(weekday)

=======
Suggestion 2

def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = input()
    index = days.index(day)
    if index < 5:
        print(5 - index)
    else:
        print(7 - index + 5)

=======
Suggestion 3

def main():
    day = input()
    week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    count = 0
    for i in range(7):
        if day == week[i]:
            count = i
            break
    if count < 5:
        print(5-count)
    else:
        print(7-count+5)

=======
Suggestion 4

def problem267_a():
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    s = input()
    print(6 - week.index(s))

=======
Suggestion 5

def main():
    weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day = input()
    print(5 - weekdays.index(day) if weekdays.index(day) < 5 else 7 - weekdays.index(day))

=======
Suggestion 6

def main():
    week = input()
    if week == "星期一":
        print(5)
    elif week == "星期二":
        print(4)
    elif week == "星期三":
        print(3)
    elif week == "星期四":
        print(2)
    elif week == "星期五":
        print(1)

=======
Suggestion 7

def main():
    week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    s = input()
    print(6 - week.index(s))

=======
Suggestion 8

def dayToSat(s):
    if s == '星期一':
        return 5
    elif s == '星期二':
        return 4
    elif s == '星期三':
        return 3
    elif s == '星期四':
        return 2
    elif s == '星期五':
        return 1
    else:
        return 0

=======
Suggestion 9

def solve():
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    s = input()
    print(7 - days.index(s))

=======
Suggestion 10

def main():
    weeks = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    week = input()
    week_index = weeks.index(week)
    print(6 - week_index)
