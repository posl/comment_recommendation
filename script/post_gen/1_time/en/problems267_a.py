Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    days = 0
    if s == 'Monday':
        days = 5
    elif s == 'Tuesday':
        days = 4
    elif s == 'Wednesday':
        days = 3
    elif s == 'Thursday':
        days = 2
    elif s == 'Friday':
        days = 1
    print(days)

=======
Suggestion 2

def main():
    # Write your code here
    day = input()
    if day == 'Monday':
        print(5)
    elif day == 'Tuesday':
        print(4)
    elif day == 'Wednesday':
        print(3)
    elif day == 'Thursday':
        print(2)
    elif day == 'Friday':
        print(1)
    else:
        print(0)
main()

=======
Suggestion 3

def main():
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    S = input()
    print(week.index('Saturday') - week.index(S) + 1)

=======
Suggestion 4

def main():
    #write your code here
    day = input()
    if day == "Monday":
        print("5")
    elif day == "Tuesday":
        print("4")
    elif day == "Wednesday":
        print("3")
    elif day == "Thursday":
        print("2")
    elif day == "Friday":
        print("1")
    else:
        print("0")
main()

=======
Suggestion 5

def main():
    #Write code here
    days = {"Monday": 5, "Tuesday": 4, "Wednesday": 3, "Thursday": 2, "Friday": 1}
    print(days[input()])

=======
Suggestion 6

def main():
    day = input()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print(6 - days.index(day))

=======
Suggestion 7

def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = input()
    print(5+days.index(day))

=======
Suggestion 8

def main():
    weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    day = input()
    print(5 - weekday.index(day))

=======
Suggestion 9

def days_to_saturday(s):
    days = 0
    while s != "Saturday":
        s = next_day(s)
        days += 1
    return days

=======
Suggestion 10

def main():
    # Write your code here
    pass
