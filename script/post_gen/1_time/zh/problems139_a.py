Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    count = 0
    for i in range(3):
        if S[i] == T[i]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    s = input()
    t = input()
    count = 0
    for i in range(3):
        if s[i] == t[i]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    s = input()
    t = input()
    cnt = 0
    for i in range(3):
        if s[i] == t[i]:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] == T[i]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    # 读取输入
    S = input()
    T = input()
    # 初始化计数器
    count = 0
    # 逐个比较S和T的字符
    for i in range(len(S)):
        if S[i] == T[i]:
            count += 1
    # 输出结果
    print(count)

=======
Suggestion 6

def main():
    # 天气预报
    S = input()
    # 实际天气
    T = input()
    # 预测正确的天数
    correct_days = 0
    for i in range(3):
        if S[i] == T[i]:
            correct_days += 1
    print(correct_days)
