Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    days = {'SUN': 7, 'MON': 6, 'TUE': 5, 'WED': 4, 'THU': 3, 'FRI': 2, 'SAT': 1}
    s = input()
    print(days[s])

=======
Suggestion 2

def main():
    S = input()
    if S == 'SUN':
        print(7)
    elif S == 'MON':
        print(6)
    elif S == 'TUE':
        print(5)
    elif S == 'WED':
        print(4)
    elif S == 'THU':
        print(3)
    elif S == 'FRI':
        print(2)
    elif S == 'SAT':
        print(1)
    else:
        print('Error')

=======
Suggestion 3

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
    else:
        print('Please input a valid day')

=======
Suggestion 4

def main():
    S = input()
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    print(7 - days.index(S))

main()

=======
Suggestion 5

def main():
    S = input()
    day = {"SUN": 0, "MON": 1, "TUE": 2, "WED": 3, "THU": 4, "FRI": 5, "SAT": 6}
    print(7 - day[S])

=======
Suggestion 6

def main():
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    today = input()
    print(7 - days.index(today))

=======
Suggestion 7

def main():
    day = input()
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(7 - week.index(day))

=======
Suggestion 8

def main():
    # Write your code here
    s = input()
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(days.index("SUN") - days.index(s) + 7)

=======
Suggestion 9

def nextSunday(s):
    day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    return (7 - day.index(s)) % 7

=======
Suggestion 10

def main():

    # Read input
    s = input()

    # Define dictionary
    days = {'SUN': 7, 'MON': 6, 'TUE': 5, 'WED': 4, 'THU': 3, 'FRI': 2, 'SAT': 1}

    # Print result
    print(days[s])
