Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    s = input()
    print(7 - week.index(s))

=======
Suggestion 2

def problem146_a():
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    s = input()
    print(7 - week.index(s))

=======
Suggestion 3

def main():
    s = input()
    day = 0
    if s == "SUN":
        day = 7
    elif s == "MON":
        day = 6
    elif s == "TUE":
        day = 5
    elif s == "WED":
        day = 4
    elif s == "THU":
        day = 3
    elif s == "FRI":
        day = 2
    elif s == "SAT":
        day = 1
    print(day)

=======
Suggestion 4

def main():
    s = input()
    if s == 'SUN':
        print(7)
    elif s == 'MON':
        print(6)
    elif s == 'TUE':
        print(5)
    elif s == 'WED':
        print(4)
    elif s == 'THU':
        print(3)
    elif s == 'FRI':
        print(2)
    elif s == 'SAT':
        print(1)

=======
Suggestion 5

def main():
    week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    S = input()
    print(7-week.index(S))

=======
Suggestion 6

def get_next_sunday(s):
    days = {'SUN':0, 'MON':1, 'TUE':2, 'WED':3, 'THU':4, 'FRI':5, 'SAT':6}
    return 7 - days[s]

=======
Suggestion 7

def next_day(day):
    if day == "SUN":
        return 7
    elif day == "MON":
        return 6
    elif day == "TUE":
        return 5
    elif day == "WED":
        return 4
    elif day == "THU":
        return 3
    elif day == "FRI":
        return 2
    elif day == "SAT":
        return 1

=======
Suggestion 8

def main():
    day = input()
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(7 - week.index(day))
