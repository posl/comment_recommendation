Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    x = 0
    for i in range(N):
        x += A[i]
        ans = max(ans, x)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    B[0] = A[0]
    for i in range(1,N):
        B[i] = B[i-1] + A[i]
    print(max(B))

=======
Suggestion 3

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    tmp = 0
    for i in range(n):
        tmp += a[i]
        ans = max(ans, tmp)
    print(ans)
    return 0

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    tmp = 0
    for i in range(N):
        tmp += A[i]
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max = 0
    now = 0
    for i in range(N):
        now += A[i]
        if now > max:
            max = now
    print(max)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_position = 0
    position = 0
    for i in range(N):
        position += A[i]
        max_position = max(max_position, position)
    print(max_position)

=======
Suggestion 7

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_max = 0
    a_sum = 0
    for a in a_list:
        a_sum += a
        a_max = max(a_max, a_sum)
    print(a_max)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    m = 0
    s = 0
    for i in range(n):
        s += a[i]
        if s > p:
            p = s
        if s < m:
            m = s
    print(p - m)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    max_val = 0
    for i in range(n):
        ans += a[i]
        max_val = max(max_val, ans)
    print(max_val)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int,input().split()))
    now = 0
    max_x = 0
    for i in range(n):
        now += a[i]
        max_x = max(max_x,now)
    print(max_x)
