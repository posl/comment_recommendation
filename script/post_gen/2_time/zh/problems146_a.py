Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    print(7 - week.index(s))

=======
Suggestion 2

def main():
    # 读取输入
    week = input().strip()
    # 处理
    week_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    week_index = week_list.index(week)
    day = 7 - week_index
    # 输出
    print(day)

=======
Suggestion 3

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
Suggestion 4

def main():
    s = input()
    day = {'SUN':7, 'MON':6, 'TUE':5, 'WED':4, 'THU':3, 'FRI':2, 'SAT':1}
    print(day[s])

=======
Suggestion 5

def main():
    day = input()
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    print(7 - week.index(day))

=======
Suggestion 6

def problem146_a():
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    s = input()
    print(7 - week.index(s))

=======
Suggestion 7

def main():
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    S = input()
    print(7 - week.index(S))

=======
Suggestion 8

def main():
    S = input()
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    print(7 - week.index(S))

=======
Suggestion 9

def main():
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    s = input()
    print(7 - week.index(s))
