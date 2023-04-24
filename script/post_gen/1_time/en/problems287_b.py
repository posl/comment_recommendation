Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = 0
    for s in S:
        if s[-3:] in T:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = 0
    for s in S:
        for t in T:
            if s[-3:] == t:
                ans += 1
                break
    print(ans)

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
                break
    print(ans)

=======
Suggestion 4

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
                break
    print(ans)

main()

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]

    ans = 0
    for i in range(n):
        if s[i][-3:] in t:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = [0] * N
    for i in range(N):
        for j in range(M):
            if S[i][3:] == T[j]:
                ans[i] = 1
    print(sum(ans))

=======
Suggestion 9

def main():
    #input
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    #compute
    ans = 0
    for s in S:
        for t in T:
            if s[-3:] == t:
                ans += 1
                break
    #output
    print(ans)
