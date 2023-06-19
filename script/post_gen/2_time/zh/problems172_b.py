Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)

=======
Suggestion 2

def solve(s,t):
    res = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            res += 1
    return res

=======
Suggestion 3

def main():
    s = input()
    t = input()
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    s = input()
    t = input()
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] != t[i]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    # 输入
    S = input()
    T = input()
    # 计算
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    # 输出
    print(count)

=======
Suggestion 7

def main():
    # S = "cupofcoffee"
    # T = "cupofhottea"
    S = input()
    T = input()
    cnt = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    s = input()
    t = input()
    cnt = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            cnt += 1
    print(cnt)
