Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    S = list(S)
    count = 0
    max_count = 0
    for i in range(3):
        if S[i] == 'R':
            count += 1
            max_count = max(count, max_count)
        else:
            count = 0
    print(max_count)

=======
Suggestion 2

def main():
    s = input()
    print(s.count('R'))

=======
Suggestion 3

def main():
    # 读取输入
    S = input()
    # 初始化
    count = 0
    max_count = 0
    # 遍历字符串
    for s in S:
        # 如果是R，计数加一
        if s == 'R':
            count += 1
        # 如果是S，计数归零
        else:
            count = 0
        # 更新最大值
        max_count = max(max_count, count)
    # 输出最大值
    print(max_count)

=======
Suggestion 4

def main():
    s = input()
    ans = 0
    cnt = 0
    for i in range(3):
        if s[i] == 'R':
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print(0)
    elif s[0] == s[1] or s[1] == s[2]:
        print(1)
    else:
        print(2)

=======
Suggestion 6

def max_rainy_days(s):
    """
    >>> max_rainy_days('RRS')
    2
    >>> max_rainy_days('SSS')
    0
    >>> max_rainy_days('RSR')
    1
    """
    return s.count('R')

=======
Suggestion 7

def main():
    weather = input()
    rain_day = 0
    max_rain_days = 0
    for i in range(3):
        if weather[i] == "R":
            rain_day += 1
            if rain_day > max_rain_days:
                max_rain_days = rain_day
        else:
            rain_day = 0
    print(max_rain_days)

=======
Suggestion 8

def main():
    S = input()
    print(S.count("R"))

=======
Suggestion 9

def main():
    s = input()
    if s == 'RRR':
        print(3)
    elif s == 'RRS' or s == 'SRR':
        print(2)
    elif s == 'SSS':
        print(0)
    else:
        print(1)

=======
Suggestion 10

def main():
    S = input()
    S = list(S)
    count = 0
    max_count = 0
    for i in range(3):
        if S[i] == 'R':
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)
