Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print(0)
    elif s[0] == s[1] or s[1] == s[2]:
        print(1)
    else:
        print(2)

=======
Suggestion 2

def main():
    s = input()
    cnt = 0
    max_cnt = 0
    for i in s:
        if i == 'R':
            cnt += 1
        else:
            cnt = 0
        if cnt > max_cnt:
            max_cnt = cnt
    print(max_cnt)

main()

=======
Suggestion 3

def solve():
    s = input()
    count = 0
    max = 0
    for i in range(3):
        if s[i] == 'R':
            count += 1
        else:
            count = 0
        if max < count:
            max = count
    print(max)

=======
Suggestion 4

def main():
    s = input()
    count = 0
    maxcount = 0
    for i in range(3):
        if s[i] == 'R':
            count += 1
            if count >= maxcount:
                maxcount = count
        else:
            count = 0
    print(maxcount)

=======
Suggestion 5

def main():
    s = input()
    print(s.count('R'))

=======
Suggestion 6

def main():
    S = input()
    print(S.count("R"))

=======
Suggestion 7

def max_rainy_days(s):
    if s == 'RRR':
        return 3
    elif s == 'RRS' or s == 'SRR':
        return 2
    elif s == 'SSS':
        return 0
    else:
        return 1

=======
Suggestion 8

def main():
    # 读取输入
    S = input()
    # 计数器
    count = 0
    # 最大值
    max_count = 0
    # 遍历字符串
    for i in range(len(S)):
        # 如果是R
        if S[i] == "R":
            # 计数器加1
            count += 1
            # 如果计数器大于最大值
            if count > max_count:
                # 重新赋值最大值
                max_count = count
        # 如果不是R
        else:
            # 重置计数器
            count = 0
    # 输出最大值
    print(max_count)

=======
Suggestion 9

def get_max_rainy_days(str):
    max_rainy_days = 0
    rainy_days = 0
    for s in str:
        if s == 'R':
            rainy_days += 1
        else:
            if rainy_days > max_rainy_days:
                max_rainy_days = rainy_days
            rainy_days = 0
    if rainy_days > max_rainy_days:
        max_rainy_days = rainy_days
    return max_rainy_days

str = input()
print(get_max_rainy_days(str))
