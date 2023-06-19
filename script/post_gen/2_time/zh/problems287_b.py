Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(m):
        t.append(input())
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:] == t[j]:
                count += 1
    print(count)

=======
Suggestion 2

def input():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    return N, M, S, T

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a.append(input())
    for i in range(m):
        b.append(input())
    count = 0
    for i in range(n):
        for j in range(m):
            if a[i][3:6] == b[j]:
                count += 1
    print(count)

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(m):
        t.append(input())
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:] == t[j] or s[i][4:] == t[j] or s[i][5:] == t[j]:
                count += 1
    print(count)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:] == t[j]:
                count += 1
    print(count)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                count += 1
    print(count)

=======
Suggestion 8

def get_last_three_char(s):
    return s[-3:]

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    ans = 0
    for i in s:
        for j in t:
            if i[-3:] == j:
                ans += 1
    print(ans)
