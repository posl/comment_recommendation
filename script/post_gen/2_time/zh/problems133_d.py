Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        if i % 2 == 0:
            ans[0] += nums[i]
            ans[1] += nums[i]
        else:
            ans[0] -= nums[i]
            ans[1] -= nums[i]
    for i in range(1, n - 1):
        ans[i] = 2 * nums[i - 1] - ans[i - 1]
    print(' '.join(map(str, ans)))


solve()

=======
Suggestion 2

def solve(n, a):
    #n = int(input())
    #a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if i % 2 == 0:
            b[0] += a[i]
        else:
            b[0] -= a[i]
    for i in range(1, n):
        b[i] = 2 * a[i-1] - b[i-1]
    print(*b)

n = int(input())
a = list(map(int, input().split()))
solve(n, a)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    for i in range(n):
        print(s - 2 * a[i], end=' ')

=======
Suggestion 4

def solve(n, a):
    b = [0] * n
    for i in xrange(n):
        if i % 2 == 0:
            b[0] += a[i]
            b[1] -= a[i]
        else:
            b[0] -= a[i]
            b[1] += a[i]
    for i in xrange(1, n - 1):
        b[i + 1] = 2 * a[i] - b[i]
    return b

n = int(raw_input())
a = map(int, raw_input().split())
print " ".join(map(str, solve(n, a)))

=======
Suggestion 5

def problem133_d():
    pass

=======
Suggestion 6

def solve(N, A):
    ans = [0] * N
    for i in range(N):
        ans[i] = A[i] - (A[i-1] + A[(i+1)%N]) // 2
    return ans

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = a[i] * 2 - ans[i-1]
    print(*ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = sum(a) - 2 * sum(a[1::2])
    for i in range(1, n):
        b[i] = 2 * a[i - 1] - b[i - 1]
    print(*b)

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    R = [0] * N
    for i in range(N):
        R[i] = A[i] * 2

    for i in range(N):
        R[i] -= R[i - 1]

    print(' '.join(map(str, R)))
