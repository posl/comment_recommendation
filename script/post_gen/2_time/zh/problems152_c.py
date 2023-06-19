Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    P = input().split()
    P = [int(i) for i in P]
    count = 0
    for i in range(1, N+1):
        if P[i-1] <= i:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    min_p = p[0]
    count = 1
    for i in range(1, n):
        if min_p >= p[i]:
            count += 1
        min_p = min(min_p, p[i])
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    min_num = P[0]
    count = 1
    for i in range(1, N):
        if P[i] <= min_num:
            count += 1
            min_num = P[i]
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    min_p = n + 1
    for i in range(n):
        if min_p > p[i]:
            count += 1
            min_p = p[i]
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min_p = p[0]
    for i in range(n):
        if min_p >= p[i]:
            ans += 1
            min_p = p[i]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 1
    min = p[0]
    for i in range(1, n):
        if p[i] <= min:
            min = p[i]
            count += 1
    print(count)

=======
Suggestion 7

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min_p = n + 1
    for i in range(n):
        if p[i] <= min_p:
            min_p = p[i]
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    min = 0
    for i in range(n):
        if i == 0:
            min = p[i]
            count += 1
        else:
            if p[i] <= min:
                count += 1
                min = p[i]
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int,input().split()))
    count = 0
    min = N+1
    for i in range(N):
        if P[i] < min:
            count += 1
            min = P[i]
    print(count)

=======
Suggestion 10

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    min_ = p[0]
    ans = 1
    for i in range(1, n):
        if p[i] <= min_:
            ans += 1
        min_ = min(min_, p[i])
    print(ans)
