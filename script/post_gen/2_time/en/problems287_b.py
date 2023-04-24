Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = 0
    for s in S:
        if any(t in s for t in T):
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:6] == t[j]:
                ans += 1
    print(ans)

=======
Suggestion 3

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
Suggestion 4

def readinput():
    n,m=input().split()
    n=int(n)
    m=int(m)
    s=[]
    for _ in range(n):
        s.append(input())
    t=[]
    for _ in range(m):
        t.append(input())
    return n,m,s,t

=======
Suggestion 5

def main():
    n,m = map(int, input().split())
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
Suggestion 6

def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    result = 0
    for i in range(N):
        for j in range(M):
            if S[i][3:6] == T[j]:
                result += 1
    print(result)
main()

=======
Suggestion 7

def main():
    n,m = map(int, input().split())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(m):
        t.append(input())
    s.sort()
    t.sort()
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:6] == t[j]:
                ans += 1
                break
    print(ans)
main()

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    print(sum(1 for i in s if i[-3:] in t))

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    s.sort()
    t.sort()
    i, j = 0, 0
    ans = 0
    while i < n and j < m:
        if s[i] < t[j]:
            i += 1
        elif s[i] > t[j]:
            j += 1
        else:
            ans += 1
            i += 1
            j += 1
    print(ans)

=======
Suggestion 10

def main():
    #input
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]

    #compute
    s.sort()
    t.sort()
    ans = 0
    i = 0
    j = 0
    while i < n and j < m:
        if s[i] == t[j]:
            ans += 1
            i += 1
            j += 1
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1

    #output
    print(ans)
