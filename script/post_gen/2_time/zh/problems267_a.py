Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    d = input()
    if(d == "星期一"):
        print(5)
    elif(d == "星期二"):
        print(4)
    elif(d == "星期三"):
        print(3)
    elif(d == "星期四"):
        print(2)
    elif(d == "星期五"):
        print(1)

=======
Suggestion 2

def main():
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    s = input()
    for i in range(len(day)):
        if s == day[i]:
            print(5 - i)
            break

=======
Suggestion 3

def main():
    day = input()
    week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    for i in range(7):
        if day == week[i]:
            print(7 - i)
            break

=======
Suggestion 4

def main():
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    day = input()
    print(6 - week.index(day))

=======
Suggestion 5

def main():
    week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    week = week + week
    s = input()
    print(week.index('Saturday') - week.index(s) + 1)

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
    else:
        print(0)

=======
Suggestion 7

def main():
    day = input()
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    week.reverse()
    print(week.index(day) + 1)

=======
Suggestion 8

def main():
    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    day = input()
    print(6 - days.index(day))

=======
Suggestion 9

def main():
    day = raw_input()
    if day == "Monday":
        print 5
    elif day == "Tuesday":
        print 4
    elif day == "Wednesday":
        print 3
    elif day == "Thursday":
        print 2
    elif day == "Friday":
        print 1
    else:
        print 0

=======
Suggestion 10

def solution(s):
    days = ['monday','tuesday','wednesday','thursday','friday']
    if s == 'saturday':
        print(0)
    elif s == 'sunday':
        print(1)
    else:
        print(days.index('friday') - days.index(s) + 2)
