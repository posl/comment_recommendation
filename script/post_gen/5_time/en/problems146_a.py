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
    elif S == "SAT":
        print(1)

=======
Suggestion 2

def main():
    S = input()
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(7 - week.index(S))

=======
Suggestion 3

def main():
    S = input()
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    print(7 - days.index(S))

=======
Suggestion 4

def main():
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    s = input()
    print(7 - week.index(s))

=======
Suggestion 5

def main():
    S = input()
    print(7 - ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"].index(S))

=======
Suggestion 6

def main():
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(7 - days.index(input()))

=======
Suggestion 7

def main():
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    S = input()
    print(7 - week.index(S))

main()

=======
Suggestion 8

def get_days_to_next_sunday(day):
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    return 7 - days.index(day)

=======
Suggestion 9

def main():
    # Take input Here and Call solution function
    s = input()
    print(solution(s))

=======
Suggestion 10

def main():
    # Take input Here and Call solution function
    s = input()
    # print(solution(s))
    print(solution(s))
