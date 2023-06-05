Synthesizing 10/10 solutions

=======
Suggestion 1

def problems152_c():
    N = int(input())
    P = list(map(int, input().split()))
    count = 1
    min = P[0]
    for i in range(1, N):
        if P[i] <= min:
            count += 1
        if P[i] < min:
            min = P[i]
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    P = list(map(int, input().split()))
    min = N
    count = 0
    for i in range(N):
        if P[i] < min:
            min = P[i]
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    min = N + 1
    count = 0
    for i in range(N):
        if P[i] < min:
            min = P[i]
            count += 1
    print(count)

main()

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int,input().split()))
    count = 0
    min = p[0]
    for i in range(n):
        if p[i] <= min:
            count += 1
            min = p[i]
    print(count)

=======
Suggestion 5

def solve(n, p):
    max = 0
    cnt = 0
    for i in range(n):
        if p[i] > max:
            max = p[i]
            cnt += 1
    return cnt

n = int(input())
p = list(map(int, input().split()))
print(solve(n, p))

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min = p[0]
    for i in range(n):
        if min >= p[i]:
            ans += 1
        if min > p[i]:
            min = p[i]
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    min = 0
    count = 0
    for i in range(n):
        if p[i] > min:
            count += 1
        min = p[i] if p[i] < min or min == 0 else min
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    min = p[0]
    count = 1
    for i in range(1, n):
        if p[i] < min:
            min = p[i]
            count += 1
    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    m = 2 * 10 ** 5 + 1
    for i in range(n):
        if p[i] < m:
            ans += 1
            m = p[i]
    print(ans)

=======
Suggestion 10

def get_input():
    N = int(input())
    P = list(map(int, input().split()))
    return N, P
