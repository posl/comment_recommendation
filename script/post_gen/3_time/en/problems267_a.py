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
    elif day == 'Saturday':
        print(0)
    elif day == 'Sunday':
        print(0)

=======
Suggestion 2

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
    elif day == "Saturday":
        print("0")
    elif day == "Sunday":
        print("0")

=======
Suggestion 3

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

=======
Suggestion 4

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
    else:
        print(0)

=======
Suggestion 5

def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    s = input()
    print(6 - days.index(s))

=======
Suggestion 6

def main():
    days = {'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5}
    s = input()
    print(days[s])

=======
Suggestion 7

def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    day = input()
    print(5 - days.index(day))

=======
Suggestion 8

def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = input()
    print(5+days.index(day))

=======
Suggestion 9

def main():
    day = input()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    idx = days.index(day)
    if idx >= 5:
        print(7 - idx)
    else:
        print(6 - idx)

=======
Suggestion 10

def main():
    #Read in the day of the week
    day = input()
    #Create a dictionary to map the day of the week to an integer
    days = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4}
    print(5 - days[day])
