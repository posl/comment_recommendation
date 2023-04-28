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
    elif s == "Saturday":
        print(0)
    elif s == "Sunday":
        print(6)
    else:
        print("Invalid input")
main()

=======
Suggestion 2

def main():
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

=======
Suggestion 3

def main():
    s = input()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(7 - days.index(s))

=======
Suggestion 4

def main():
    S = input()
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(6 - week.index(S))

=======
Suggestion 5

def main():
    day = input()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(days.index('Saturday') - days.index(day))

=======
Suggestion 6

def main():
    s = input()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    print(days.index('Saturday') - days.index(s))

=======
Suggestion 7

def main():
    s = input().strip()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(6 - days.index(s))

=======
Suggestion 8

def main():
    s = input()
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    week = week + week
    for i in range(7):
        if s == week[i]:
            print(7-i)
            break

=======
Suggestion 9

def main():
    # Take input
    S = input()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(7 - days.index(S))

=======
Suggestion 10

def problem267_a():
    S = input()
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    print(7 - days.index(S))
