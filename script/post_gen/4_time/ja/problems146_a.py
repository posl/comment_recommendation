Synthesizing 10/10 solutions

=======
Suggestion 1

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
    return

main()

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
    S = input()
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(7 - week.index(S))

=======
Suggestion 6

def get_next_day(day):
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
    else:
        return 0

s = input()
print(get_next_day(s))

=======
Suggestion 7

def main():
    s = input()
    week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    print(7-week.index(s))

=======
Suggestion 8

def main():
    S = input()
    day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    print(7 - day.index(S))

=======
Suggestion 9

def main():
    s = input()
    day_list = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    print(7-day_list.index(s))

=======
Suggestion 10

def get_next_sunday(s):
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    return 7 - day.index(s)
