Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_day_index(day):
    day_index = 0
    if day == 'SUN':
        day_index = 0
    elif day == 'MON':
        day_index = 1
    elif day == 'TUE':
        day_index = 2
    elif day == 'WED':
        day_index = 3
    elif day == 'THU':
        day_index = 4
    elif day == 'FRI':
        day_index = 5
    elif day == 'SAT':
        day_index = 6
    return day_index

=======
Suggestion 2

def get_days(s):
    days = {
        'SUN': 7,
        'MON': 6,
        'TUE': 5,
        'WED': 4,
        'THU': 3,
        'FRI': 2,
        'SAT': 1
    }
    return days[s]

=======
Suggestion 3

def main():
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    s = input()
    print(7 - week.index(s))

=======
Suggestion 4

def main():
    week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    s = input()
    print(7-week.index(s))

=======
Suggestion 5

def main():
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    a = input()
    print(7 - week.index(a))

=======
Suggestion 6

def main():
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    S = input()
    print(7-week.index(S))

=======
Suggestion 7

def main():
    # 读取输入
    s = input()
    # 请在此添加代码
    day = 0
    # 请在此添加代码
    if s == 'SUN':
        day = 7
    elif s == 'MON':
        day = 6
    elif s == 'TUE':
        day = 5
    elif s == 'WED':
        day = 4
    elif s == 'THU':
        day = 3
    elif s == 'FRI':
        day = 2
    elif s == 'SAT':
        day = 1
    # 请在此添加代码
    print(day)

=======
Suggestion 8

def main():
    S = input()
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    print(7 - week.index(S))
