Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, N+1):
        if a[i-1] == i:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if a[i-1] == i:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] <= i+1:
            continue
        if a[a[i]-1] == i+1:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N + 1):
        if i == A[A[i - 1] - 1]:
            ans += 1
    print(ans // 2)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] == i+1:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > i + 1:
            continue
        if A[A[i] - 1] == i + 1:
            ans += 1
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if A[i] == i + 1:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    ans = 0
    for i in range(N):
        if i+1 == As[As[i]-1]:
            ans += 1

    # output
    print(ans//2)

=======
Suggestion 9

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    d = {}
    for i in range(N):
        l = i + a[i]
        r = i - a[i]
        if l in d:
            d[l] += 1
        else:
            d[l] = 1
        if r in d:
            ans += d[r]
    print(ans)
