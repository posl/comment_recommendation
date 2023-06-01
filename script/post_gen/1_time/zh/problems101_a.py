Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    sum = 0
    for c in s:
        if c == '+':
            sum += 1
        else:
            sum -= 1
    print(sum)

=======
Suggestion 3

def main():
    S = input()
    print(S.count('+') - S.count('-'))

=======
Suggestion 4

def main():
    s = input()
    num = 0
    for i in range(4):
        if s[i] == "+":
            num += 1
        else:
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
    s = input()
    print(s.count('+') - s.count('-'))

=======
Suggestion 7

def main():
    s = input()
    count = 0
    for i in s:
        if i == '+':
            count += 1
        else:
            count -= 1
    print(count)

=======
Suggestion 8

def main():
    S = input()
    sum = 0
    for i in range(0,4):
        if S[i] == '+':
            sum += 1
        else:
            sum -= 1
    print(sum)

=======
Suggestion 9

def main():
    # 读取输入
    s = input()
    # 计算结果
    result = 0
    for c in s:
        if c == '+':
            result += 1
        else:
            result -= 1
    # 输出结果
    print(result)

=======
Suggestion 10

def main():
    # 读取输入
    s = input()
    # 初始值
    result = 0
    # 计算结果
    for i in range(4):
        if s[i] == '+':
            result += 1
        else:
            result -= 1
    # 输出结果
    print(result)
