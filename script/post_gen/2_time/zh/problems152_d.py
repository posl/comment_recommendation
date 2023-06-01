Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    min_P = N+1
    count = 0
    for i in range(N):
        if P[i] <= min_P:
            min_P = P[i]
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    P = list(map(int,input().split()))
    count = 1
    min = P[0]
    for i in range(1,N):
        if P[i] <= min:
            count += 1
            min = P[i]
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    min = N
    for i in range(N):
        if P[i] <= min:
            count += 1
            min = P[i]
    print(count)

=======
Suggestion 4

def get_input():
    n = int(input())
    p = [int(x) for x in input().split()]
    return n, p

=======
Suggestion 5

def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    count = 0
    min = N + 1
    for i in range(N):
        if P[i] <= min:
            count += 1
            min = P[i]
    print(count)

=======
Suggestion 6

def solve():
    N = int(input())
    P = list(map(int, input().split()))
    min_val = N + 1
    ans = 0
    for i in range(N):
        if P[i] <= min_val:
            ans += 1
            min_val = P[i]
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    P = list(map(int, input().split()))
    print(solve(N, P))

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    m = p[0]
    for i in range(n):
        if p[i] <= m:
            ans += 1
            m = p[i]
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 1
    min = p[0]
    for i in range(1, n):
        if min >= p[i]:
            ans += 1
            min = p[i]
    print(ans)

=======
Suggestion 10

def solve():
    N = int(input())
    P = list(map(int, input().split()))
    min_p = N + 1
    ans = 0
    for p in P:
        if p <= min_p:
            ans += 1
            min_p = p
    print(ans)
