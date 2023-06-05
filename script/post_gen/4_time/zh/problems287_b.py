Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                count += 1
    print(count)

=======
Suggestion 2

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
Suggestion 3

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(M):
        T.append(input())

    #print(N)
    #print(M)
    #print(S)
    #print(T)

    count = 0
    for i in range(M):
        for j in range(N):
            if T[i] == S[j]:
                count += 1
                break
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
            if s[i][3:] == t[j] or s[i][4:] == t[j] or s[i][5:] == t[j]:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if S[i][-3:] == T[j]:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    cnt = 0
    for i in range(M):
        for j in range(N):
            if S[j][3:] == T[i]:
                cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                ans += 1
                break
    print(ans)

=======
Suggestion 9

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
            if s[i][3:6] == t[j]:
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
    count = 0
    for i in range(m):
        for j in range(n):
            if t[i] == s[j][-3:]:
                count += 1
    print(count)
