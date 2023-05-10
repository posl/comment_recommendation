Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    ans = 0
    if s == "SUN":
        ans = 7
    elif s == "MON":
        ans = 6
    elif s == "TUE":
        ans = 5
    elif s == "WED":
        ans = 4
    elif s == "THU":
        ans = 3
    elif s == "FRI":
        ans = 2
    elif s == "SAT":
        ans = 1
    print(ans)

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
    else:
        print(1)

=======
Suggestion 3

def main():
    S = input()
    week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    print(7 - week.index(S))

=======
Suggestion 4

def main():
    s = input()

    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(7 - week.index(s))

=======
Suggestion 5

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
Suggestion 6

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
Suggestion 7

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
    elif S == "SAT":
        print(1)

=======
Suggestion 8

def get_next_sunday(s):
    if s == "SUN":
        return 7
    elif s == "MON":
        return 6
    elif s == "TUE":
        return 5
    elif s == "WED":
        return 4
    elif s == "THU":
        return 3
    elif s == "FRI":
        return 2
    elif s == "SAT":
        return 1
