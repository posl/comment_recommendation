Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    str = input()
    count = 0
    max = 0
    for i in str:
        if i == 'R':
            count += 1
        else:
            count = 0
        if count > max:
            max = count
    print(max)

=======
Suggestion 2

def main():
    # 读取输入
    s = input()

    # 初始化
    count = 0
    max_count = 0

    # 计数
    for i in s:
        if i == "R":
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0

    # 打印最大值
    print(max_count)

=======
Suggestion 3

def main():
    # 读取输入
    s = input()
    # 处理
    # 通过字符串的count方法，计算R出现的次数
    # 通过max方法，计算最大值
    max_count = max(s.count('R'), s.count('S'))
    # 输出结果
    print(max_count)

=======
Suggestion 4

def main():
    S = input()
    count = 0
    max = 0
    for i in range(3):
        if S[i] == 'R':
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    if count > max:
        max = count
    print(max)

=======
Suggestion 5

def main():
    S = input()
    count = 0
    max = 0
    for i in range(3):
        if S[i] == "R":
            count = count + 1
            if count > max:
                max = count
        else:
            count = 0
    print(max)

=======
Suggestion 6

def main():
    S = input()
    print(S.count('R'))

=======
Suggestion 7

def main():
    S = input()
    print(S.count("R"))

=======
Suggestion 8

def main():
    S = input()
    if S == 'RRR':
        print(3)
    elif S == 'SRR' or S == 'RRS':
        print(2)
    elif S == 'SSS':
        print(0)
    else:
        print(1)

=======
Suggestion 9

def main():
    # 读入数据
    s = input()

    # 计算答案
    ans = 0
    for i in range(3):
        if s[i] == "R":
            ans += 1

    # 输出答案
    print(ans)
