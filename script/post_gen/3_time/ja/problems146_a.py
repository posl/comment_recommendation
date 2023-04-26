Synthesizing 10/10 solutions (Duplicates hidden)

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
    elif S == "SAT":
        print(1)

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
    else:
        print(1)

=======
Suggestion 4

def main():
    week = {"SUN": 0, "MON": 1, "TUE": 2, "WED": 3, "THU": 4, "FRI": 5, "SAT": 6}
    print(7 - week[input()])

=======
Suggestion 5

def main():
    S = input()
    d = {"SUN":7, "MON":6, "TUE":5, "WED":4, "THU":3, "FRI":2, "SAT":1}
    print(d[S])

=======
Suggestion 6

def main():
    S = input()
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(7 - days.index(S))

=======
Suggestion 7

def main():
    #入力
    S = input()
    #出力
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
