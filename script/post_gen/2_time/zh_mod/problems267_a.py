Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    #input
    today = input()
    #today = 'Wednesday'
    #process
    if today == 'Monday':
        print('5')

=======
Suggestion 2

def main():
    day = input()
    if day == "Monday":
        print(5)
    elif day == "Tuesday":
        print(4)
    elif day == "Wedne

=======
Suggestion 3

def solve(day):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return 7 - days.index(day)

=======
Suggestion 4

def main():
    week = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    day = int(input())
    print(week.index(day))

=======
Suggestion 5

def main():
    import sys
    import datetime
    # 读取输入
    s = sys.stdin.readline().strip()
    # 计算
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    i = week.index(s)
    # 统计天数
    days = 0
    for j in range(i, 7):
        if week[j] == 'Saturday':
            break
        days += 1
    # 输出
    print(days)

=======
Suggestion 6

def main():
    week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day = input()
    for i in ran

=======
Suggestion 7

def main():
    week = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
    s = input()
    print(week.index

=======
Suggestion 8

def main():
    s = str(input())
    list1 = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    list2 = ['Saturday','Sunday'

=======
Suggestion 9

def get_days(s):
    days = 0
    if s == "Monday":
        days = 5
    elif s == "Tuesday":
        days = 4
    elif s == "Wednesday":

=======
Suggestion 10

def get_days():
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day = input()
    day_index
