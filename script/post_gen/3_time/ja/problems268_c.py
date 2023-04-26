Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i != N-1:
                p[i], p[i+1] = p[i+1], p[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    p = [int(i) for i in input().split()]
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i < N-1:
                p[i], p[i+1] = p[i+1], p[i]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == p[i]:
            ans += 1
    if ans == n:
        print(n)
    else:
        print(ans+1)

=======
Suggestion 4

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if P[i] == i:
            ans += 1
    print(ans + (ans % 2))

=======
Suggestion 5

def main():
    N = int(input())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            if i != 0 and i != N-1:
                if p[i-1] != i-1 and p[i+1] != i+1:
                    p[i] = i-1
                    ans += 1
            elif i == 0:
                if p[i+1] != i+1:
                    p[i] = i+1
                    ans += 1
            elif i == N-1:
                if p[i-1] != i-1:
                    p[i] = i-1
                    ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if i == p[i]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    P = list(map(int, input().split()))
    A = [0]*N
    for i in range(N):
        A[P[i]] = i
    #print(A)
    #print(P)
    ans = 1
    for i in range(N-1):
        if A[i+1] - A[i] == 1:
            pass
        else:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    p = list(map(int,input().split()))
    #print(N,p)
    cnt = 0
    for i in range(N):
        if p[i] == i:
            cnt += 1
    if cnt == N:
        print(cnt)
    elif cnt == N-2:
        print(cnt+2)
    else:
        print(cnt+1)

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    d = [0] * n
    for i, v in enumerate(p):
        d[v] = i
    res = 0
    for i in range(n):
        if d[i] == i:
            res += 1
    print(res)
