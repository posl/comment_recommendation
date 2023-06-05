Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取输入
    S = input()

    # 初始化
    ans = 0
    # 吃符号
    for i in range(len(S)):
        if S[i] == '+':
            ans += 1
        elif S[i] == '-':
            ans -= 1
        else:
            pass
    # 输出答案
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    count = 0
    for i in S:
        if i == '+':
            count += 1
        else:
            count -= 1
    print(count)

=======
Suggestion 3

def solve():
    s = input()
    ans = 0
    for c in s:
        if c == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == '+':
            count += 1
        else:
            count -= 1
    print(count)

=======
Suggestion 5

def main():
    S = input()
    print(S.count('+') - S.count('-'))

=======
Suggestion 6

def main():
    S = input()
    sum = 0
    for i in range(0, 4):
        if S[i] == '+':
            sum += 1
        else:
            sum -= 1
    print(sum)

=======
Suggestion 7

def main():
    S = input()
    ans = 0
    for i in range(4):
        if S[i] == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)

=======
Suggestion 8

def main():
    # 输入
    S = input()
    # 逻辑
    count = 0
    for i in range(4):
        if S[i] == '+':
            count += 1
        else:
            count -= 1
    # 输出
    print(count)

=======
Suggestion 9

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
Suggestion 10

def main():
    #input
    s = input()
    #init
    res = 0
    #process
    for i in s:
        if i == "+":
            res += 1
        elif i == "-":
            res -= 1
        else:
            print("input error")
            return
    #output
    print(res)
    return
