Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 1
    min = P[0]
    for i in range(1, N):
        if P[i] <= min:
            ans += 1
            min = P[i]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 1
    min = p[0]
    for i in range(1, n):
        if p[i] < min:
            ans += 1
            min = p[i]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(n):
        if p[i] > max:
            max = p[i]
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min = N
    for i in range(N):
        if P[i] <= min:
            ans += 1
            min = P[i]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min = N+1
    for i in range(N):
        if P[i] <= min:
            ans += 1
            min = P[i]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int, input().split()))
    cnt = 0
    min = N+1
    for i in range(N):
        if min > P[i]:
            cnt += 1
            min = P[i]
    print(cnt)

=======
Suggestion 7

def main():
    N = int(input())
    P = list(map(int, input().split()))
    min = N
    count = 0
    for i in range(N):
        if P[i] < min:
            count += 1
            min = P[i]
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))
    min = n+1
    cnt = 0
    for i in range(n):
        if p[i] < min:
            cnt += 1
            min = p[i]
    print(cnt)

=======
Suggestion 9

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    m = 1
    for i in range(n):
        if m >= p[i]:
            ans += 1
        m = min(m, p[i])
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    p_list = list(map(int, input().split()))

    count = 0
    min = n+1

    for i in range(n):
        if p_list[i] < min:
            count += 1
            min = p_list[i]

    print(count)
