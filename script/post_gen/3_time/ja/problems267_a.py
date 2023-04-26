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

def calc_days(s):
    days = {
        "Monday": 5,
        "Tuesday": 4,
        "Wednesday": 3,
        "Thursday": 2,
        "Friday": 1,
        "Saturday": 0,
        "Sunday": 6
    }
    return days[s]

=======
Suggestion 3

def main():
    s = input()
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(week.index("Saturday") - week.index(s))

=======
Suggestion 4

def main():
    S = input()
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(week.index("Saturday") - week.index(S) + 7)

=======
Suggestion 5

def main():
    s = input()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(7 - days.index(s))

=======
Suggestion 6

def main():
    s = input()
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    print(5 - week.index(s))

=======
Suggestion 7

def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    s = input()
    result = 0
    for i in range(5):
        if s == days[i]:
            result = 5 - i
            break
    print(result)
main()

=======
Suggestion 8

def main():
    s = input()
    w = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    print(w.index('Saturday') - w.index(s))

=======
Suggestion 9

def problem267_a():
    S = input()
    dic = {"Monday":5,"Tuesday":4,"Wednesday":3,"Thursday":2,"Friday":1,"Saturday":0,"Sunday":6}
    print(dic[S])
    return

=======
Suggestion 10

def get_ans(s):
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    return 7 - day.index(s)
