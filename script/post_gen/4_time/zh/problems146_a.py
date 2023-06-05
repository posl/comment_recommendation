Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读取输入
    s = input()
    # 解决问题
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
    else:
        print('error')

=======
Suggestion 2

def main():
    week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    s = input()
    print(7-week.index(s))

=======
Suggestion 3

def get_next_sun_day(s):
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    return 7 - days.index(s)

=======
Suggestion 4

def main():
    # 读取输入
    s = input()
    # 计算并输出答案
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    print(7 - week.index(s))

=======
Suggestion 5

def problem146_a():
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
