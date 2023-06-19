Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    print(s.count('+') - s.count('-'))

=======
Suggestion 2

def main():
    s = input()
    ans = 0
    for i in range(4):
        if s[i] == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)

=======
Suggestion 3

def main():
    # 读取输入
    s = input()
    # 初始化
    result = 0
    # 遍历字符串
    for i in s:
        if i == '+':
            result += 1
        else:
            result -= 1
    # 打印结果
    print(result)

=======
Suggestion 4

def main():
    S = input()
    num = 0
    for i in range(4):
        if S[i] == '+':
            num += 1
        else:
            num -= 1
    print(num)

=======
Suggestion 5

def main():
    s = input()
    n = 0
    for c in s:
        if c == '+':
            n += 1
        else:
            n -= 1
    print(n)

=======
Suggestion 6

def main():
    S = input()
    result = 0
    for i in range(len(S)):
        if S[i] == '+':
            result += 1
        else:
            result -= 1
    print(result)

=======
Suggestion 7

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
Suggestion 8

def main():
    s = input()
    result = 0
    for i in s:
        if i == '+':
            result += 1
        else:
            result -= 1
    print(result)

=======
Suggestion 9

def main():
    s = input()
    sum = 0
    for i in s:
        if i == '+':
            sum += 1
        else:
            sum -= 1
    print(sum)

=======
Suggestion 10

def main():
    # 读取输入
    s = input()
    # 初始化
    result = 0
    # 处理
    for i in range(4):
        if s[i] == '+':
            result += 1
        else:
            result -= 1
    # 输出
    print(result)
