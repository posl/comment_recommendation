Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]

    ans = 0
    for s in S:
        for t in T:
            if s.endswith(t):
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]

    ans = 0
    for i in range(N):
        for j in range(M):
            if S[i][-3:] == T[j]:
                ans += 1

    print(ans)

main()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if S[i][-3:] == T[j]:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    ans = 0
    for s in S:
        for t in T:
            if s[-3:] == t:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(m):
        t.append(input())
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:] == t[j]:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    n,m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]

    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    s_list = [input() for i in range(n)]
    t_list = [input() for i in range(m)]
    count = 0
    for s in s_list:
        for t in t_list:
            if s[-3:] == t:
                count += 1
    print(count)

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(m):
        t.append(input())
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                print(i,j)
