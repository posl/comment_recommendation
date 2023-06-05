Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    cnt = 1
    for i in range(1,n):
        if s[i] != s[i-1]:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    ans = 1
    for i in range(1, N):
        if S[i-1] != S[i]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    S_list = list(S)
    S_set = set(S_list)
    print(len(S_set))

=======
Suggestion 6

def main():
    # 读入数据
    n = int(input())
    s = input()
    # 求解
    ans = 1
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            ans += 1
    # 输出结果
    print(ans)

=======
Suggestion 7

def merge(s):
    if len(s) == 1:
        return 1
    if s[0] == s[1]:
        return merge(s[1:])
    else:
        return 1 + merge(s[1:])

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    result = 1
    for i in range(1,n):
        if s[i] != s[i-1]:
            result += 1
    print(result)

=======
Suggestion 9

def merge(s):
    if len(s) == 1:
        return 1
    elif len(s) == 2:
        return 2 if s[0] != s[1] else 1
    else:
        return merge(s[:len(s)//2]) + merge(s[len(s)//2:])

n = int(input())
s = input()
print(merge(s))

=======
Suggestion 10

def findSlimeCount(s):
    if len(s) == 0:
        return 0
    res = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            res += 1
    return res
