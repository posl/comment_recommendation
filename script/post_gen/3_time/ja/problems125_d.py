Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n):
        if a[i-1] * a[i] < 0:
            cnt += 1
    if cnt == 0:
        print(sum(map(abs, a)) - 2 * min(map(abs, a)))
    else:
        print(sum(map(abs, a)))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if A[i-1] > 0:
            ans += A[i-1]
            A[i] += A[i-1]
            A[i-1] = 0
    if A[-1] > 0:
        ans += A[-1]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if a[i] < 0:
            a[i] = -a[i]
        if a[i+1] < 0:
            a[i+1] = -a[i+1]
        ans += a[i+1] - a[i]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        if a[i-1] + a[i] > 0:
            a[i] += a[i-1]
            ans += a[i-1]
        else:
            ans += a[i-1] + a[i]
            a[i] = 0
    print(ans + a[-1])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1,n):
        if a[i-1] > 0:
            ans += a[i-1]
            a[i-1] = 0
        if a[i] < 0:
            ans += a[i]
            a[i] = 0
    if a[n-1] > 0:
        ans += a[n-1]
        a[n-1] = 0
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    if N == 2:
        return max(A[0] + A[1], A[0] - A[1], -A[0] + A[1], -A[0] - A[1])

    if N == 3:
        return max(
            A[0] + A[1] + A[2],
            A[0] + A[1] - A[2],
            A[0] - A[1] + A[2],
            A[0] - A[1] - A[2],
            A[0] - A[1] - A[2],
            A[0] - A[1] - A[2],
            - A[0] + A[1] + A[2],
            - A[0] + A[1] - A[2],
            - A[0] - A[1] + A[2],
            - A[0] - A[1] - A[2],
        )

    if N % 2 == 0:
        return sum(A) + max(
            max(A),
            min(A),
            -max(A),
            -min(A),
            0
        )
    else:
        return sum(A) + max(
            max(A),
            min(A),
            -max(A),
            -min(A),
            0,
            -2 * min(A),
            -2 * max(A)
        )

print(solve())

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    neg = 0
    min_abs = 10**9
    for i in range(n):
        if a[i] < 0:
            neg += 1
        ans += abs(a[i])
        min_abs = min(min_abs, abs(a[i]))
    if neg % 2 == 0:
        print(ans)
    else:
        print(ans - min_abs*2)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    minus = 0
    for i in range(N-1):
        if A[i]+minus < 0:
            if A[i]+A[i+1]+minus < 0:
                ans += abs(A[i]+A[i+1]+minus)
                minus = -1
            else:
                ans += abs(A[i]+minus)
                minus = A[i+1]
        else:
            minus += A[i+1]
    ans += abs(A[N-1]+minus)
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    minus = 0
    min_minus = 10000000000
    for i in range(N):
        if A[i] < 0:
            minus += 1
        if abs(A[i]) < min_minus:
            min_minus = abs(A[i])
        ans += abs(A[i])
    if minus % 2 == 1:
        ans -= min_minus * 2
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))

    sum = 0
    count_minus = 0
    min = 10**9
    for i in range(n):
        if a[i] < 0:
            count_minus += 1
            a[i] *= -1
        sum += a[i]
        if min > a[i]:
            min = a[i]
    if count_minus % 2 == 0:
        print(sum)
    else:
        print(sum - min * 2)
