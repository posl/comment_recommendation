Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S == "SUN":
        print(7)
    elif S == "MON":
        print(6)
    elif S == "TUE":
        print(5)
    elif S == "WED":
        print(4)
    elif S == "THU":
        print(3)
    elif S == "FRI":
        print(2)
    else:
        print(1)

=======
Suggestion 2

def main():
    day = input()
    if day == 'SUN':
        print(7)
    elif day == 'MON':
        print(6)
    elif day == 'TUE':
        print(5)
    elif day == 'WED':
        print(4)
    elif day == 'THU':
        print(3)
    elif day == 'FRI':
        print(2)
    elif day == 'SAT':
        print(1)

=======
Suggestion 3

def main():
    day = input()
    if day == "SUN":
        print(7)
    elif day == "MON":
        print(6)
    elif day == "TUE":
        print(5)
    elif day == "WED":
        print(4)
    elif day == "THU":
        print(3)
    elif day == "FRI":
        print(2)
    elif day == "SAT":
        print(1)

=======
Suggestion 4

def main():
    S = input()
    if S == "SUN":
        print("7")
    elif S == "MON":
        print("6")
    elif S == "TUE":
        print("5")
    elif S == "WED":
        print("4")
    elif S == "THU":
        print("3")
    elif S == "FRI":
        print("2")
    elif S == "SAT":
        print("1")

=======
Suggestion 5

def main():
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    s = input()
    print(7 - days.index(s))

=======
Suggestion 6

def main():
    day = input()
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    print(7 - days.index(day))

=======
Suggestion 7

def main():
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    s = input()
    print(7 - week.index(s))

=======
Suggestion 8

def main():
    day = input()
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(7 - days.index(day))

=======
Suggestion 9

def main():
    # Get the day of the week
    day = input()
    # Create a list of the days of the week
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    # Print the number of days until the next Sunday
    print(7 - days.index(day))

=======
Suggestion 10

def main():
    # Read the input
    s = input()
    # Create a dictionary with the days of the week
    days = {'SUN': 7, 'MON': 6, 'TUE': 5, 'WED': 4, 'THU': 3, 'FRI': 2, 'SAT': 1}
    # Print the number of days before the next Sunday
    print(days[s])
