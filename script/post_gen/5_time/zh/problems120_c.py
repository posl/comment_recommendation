Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] == '1':
            ans += 1
    ans = min(ans, N-ans)
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans += 1
    print(min(ans, N - ans) * 2)

=======
Suggestion 3

def main():
    # 读取输入
    S = input()
    # 计算并输出结果
    print(calc_max_remove(S))

=======
Suggestion 4

def main():
    s = input()
    red, blue = 0, 0
    for i in range(len(s)):
        if s[i] == "0":
            red += 1
        else:
            blue += 1
    print(min(red, blue) * 2)

=======
Suggestion 5

def main():
    s = input()
    red = 0
    blue = 0
    for i in range(len(s)):
        if s[i] == "0":
            red += 1
        else:
            blue += 1
    print(min(red, blue) * 2)

=======
Suggestion 6

def main():
    s = input()
    n = len(s)
    r = s.count("0")
    b = s.count("1")
    print(min(r, b) * 2)

=======
Suggestion 7

def solve():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == '1':
            ans += 1
    ans = min(ans, n-ans)
    print(ans)
solve()

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    r = 0
    b = 0
    for i in range(n):
        if s[i] == '0':
            r += 1
        else:
            b += 1
    print(n - abs(r - b))

=======
Suggestion 9

def solve():
    S = input()
    red = S.count('0')
    blue = len(S) - red
    print(min(red, blue) * 2)

=======
Suggestion 10

def main():
    s = input()
    n = len(s)
    if n == 1:
        print(0)
        return
    count = 0
    for i in range(n):
        if s[i] == '0':
            count += 1
    print(min(count, n-count)*2)
