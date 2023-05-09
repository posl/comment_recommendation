Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    min = p[0]
    for i in range(n):
        if p[i] <= min:
            count += 1
            min = p[i]
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    min = p[0]
    for i in range(n):
        if p[i] <= min:
            cnt += 1
            min = p[i]
    print(cnt)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    min = n
    for i in range(n):
        if p[i] <= min:
            count += 1
            min = p[i]
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min = n + 1
    for i in range(n):
        if p[i] < min:
            ans += 1
            min = p[i]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    mi = p[0]
    cnt = 1
    for i in range(1, n):
        if p[i] <= mi:
            mi = p[i]
            cnt += 1
    print(cnt)
    return

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min_val = N + 1
    for i in range(N):
        if P[i] <= min_val:
            ans += 1
            min_val = P[i]
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    P = [int(i) for i in input().split()]
    count = 0
    min = 0
    for i in range(N):
        if i == 0:
            min = P[i]
            count += 1
        elif P[i] <= min:
            min = P[i]
            count += 1
    print(count)

=======
Suggestion 8

def solve():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    min = float('inf')
    for i in range(N):
        if P[i] <= min:
            count += 1
            min = P[i]
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))
    P = [0] + P
    ans = 0
    min = N + 1
    for i in range(1, N + 1):
        if P[i] < min:
            ans += 1
            min = P[i]
    print(ans)

=======
Suggestion 10

def get_int():
	return int(input())
