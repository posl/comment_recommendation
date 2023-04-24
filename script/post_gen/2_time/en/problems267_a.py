Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    S = input()
    if S == "Monday":
        print("5")
    elif S == "Tuesday":
        print("4")
    elif S == "Wednesday":
        print("3")
    elif S == "Thursday":
        print("2")
    elif S == "Friday":
        print("1")
    elif S == "Saturday":
        print("0")
    elif S == "Sunday":
        print("0")
    else:
        print("Invalid Input")

=======
Suggestion 3

def main():
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

=======
Suggestion 4

def main():
    s = input()
    if s == "Monday":
        print("5")
    elif s == "Tuesday":
        print("4")
    elif s == "Wednesday":
        print("3")
    elif s == "Thursday":
        print("2")
    elif s == "Friday":
        print("1")
    elif s == "Saturday":
        print("0")
    elif s == "Sunday":
        print("0")
    else:
        print("Error")

=======
Suggestion 5

def main():
    # Write your code here
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
    elif s == 'Saturday':
        print(0)
    elif s == 'Sunday':
        print(6)

=======
Suggestion 6

def main():
    # Write code here
    day = input()
    if day == "Monday":
        print(5)
    elif day == "Tuesday":
        print(4)
    elif day == "Wednesday":
        print(3)
    elif day == "Thursday":
        print(2)
    elif day == "Friday":
        print(1)
    else:
        print(0)

=======
Suggestion 7

def main():
    s = input()
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    if s == "Saturday" or s == "Sunday":
        print(0)
    else:
        print(week.index(s) - 5)

=======
Suggestion 8

def main():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    s = input()
    print(5 - days.index(s))

=======
Suggestion 9

def main():
    S = input()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    print(5 - days.index(S))

main()

=======
Suggestion 10

def main():
    day = input()
    dayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(dayList.index("Saturday") - dayList.index(day) + 1)
