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
    else:
        print(0)

=======
Suggestion 2

def main():
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
Suggestion 3

def main():
    S = input()
    if S == "Monday":
        print(5)
    elif S == "Tuesday":
        print(4)
    elif S == "Wednesday":
        print(3)
    elif S == "Thursday":
        print(2)
    elif S == "Friday":
        print(1)
    else:
        print(0)

=======
Suggestion 4

def main():
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
Suggestion 5

def main():
    # input
    S = input()

    # compute
    if S == 'Monday':
        ans = 5
    elif S == 'Tuesday':
        ans = 4
    elif S == 'Wednesday':
        ans = 3
    elif S == 'Thursday':
        ans = 2
    elif S == 'Friday':
        ans = 1
    else:
        ans = 6

    # output
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(6 - week.index(s))

=======
Suggestion 7

def main():
    s = input()
    day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i in range(len(day)):
        if day[i] == s:
            print(6 - i)
            break

=======
Suggestion 8

def main():
    week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    s = input()
    print(week.index('Saturday') - week.index(s))

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
    print(solution(s))
    pass
