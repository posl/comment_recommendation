Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    min = P[0]
    count = 1
    for i in range(1, N):
        if P[i] <= min:
            count += 1
            min = P[i]
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    m = 0
    for i in range(n):
        if a[i] > m:
            ans += 1
            m = a[i]
    print(ans)

=======
Suggestion 3

def problems152_c():
    N = int(input())
    P = list(map(int, input().split()))
    result = 1
    min = P[0]
    for i in range(1, N):
        if P[i] <= min:
            result += 1
            min = P[i]
    print(result)
problems152_c()

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    m = n + 1
    for i in range(n):
        if p[i] < m:
            ans += 1
            m = p[i]
    print(ans)

=======
Suggestion 5

def problems152_c():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 1
    min = p[0]
    for i in range(1, n):
        if p[i] < min:
            cnt += 1
            min = p[i]
    print(cnt)

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int, input().split()))

    min = N+1
    count = 0
    for i in range(N):
        if min > P[i]:
            count += 1
            min = P[i]
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 1
    for i in range(1, n):
        if p[i] <= p[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 1
    m = p[0]
    for i in range(1, n):
        if m >= p[i]:
            ans += 1
            m = p[i]
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    print(solve(n, p))
