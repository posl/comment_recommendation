Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    count = 0
    for i in range(0,4):
        if s[i] == '+':
            count += 1
        else:
            count -= 1
    print(count)

=======
Suggestion 2

def solve():
    s = input()
    result = 0
    for i in s:
        if i == "+":
            result += 1
        else:
            result -= 1
    print(result)
solve()

=======
Suggestion 3

def main():
    s = input()
    sum = 0
    for i in range(4):
        if s[i] == '+':
            sum += 1
        else:
            sum -= 1
    print(sum)

=======
Suggestion 4

def main():
    s = input()
    num = 0
    for i in s:
        if i == '+':
            num += 1
        elif i == '-':
            num -= 1
    print(num)

=======
Suggestion 5

def main():
    S = input()
    count = 0
    for i in range(4):
        if S[i] == '+':
            count += 1
        else:
            count -= 1
    print(count)

=======
Suggestion 6

def main():
    # 读取输入
    S = input()
    # 初始化变量
    num = 0
    # 计算
    for i in range(len(S)):
        if S[i] == '+':
            num += 1
        else:
            num -= 1
    # 输出结果
    print(num)

=======
Suggestion 7

def main():
    S = input()
    x = 0
    for i in range(4):
        if S[i] == "+":
            x += 1
        else:
            x -= 1
    print(x)

=======
Suggestion 8

def problem101_a():
    S = raw_input()
    print S.count('+') - S.count('-')

=======
Suggestion 9

def main():
    S = input()
    count = 0
    for i in S:
        if i == '+':
            count += 1
        else:
            count -= 1
    print(count)
