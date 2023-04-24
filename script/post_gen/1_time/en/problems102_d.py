Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, a):
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + a[i - 1]
    ans = float('inf')
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            ans = min(ans, abs(s[i] - s[0] - (s[j] - s[i]) - (s[n] - s[j])))
    return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0 for _ in range(n+1)]
    for i in range(n):
        s[i+1] = s[i] + a[i]
    ans = float('inf')
    for i in range(1, n-2):
        for j in range(i+1, n-1):
            ans = min(ans, abs(s[i] - s[0] - s[j] + s[i]), abs(s[i] - s[0] - s[j] + s[j] - s[i]), abs(s[i] - s[0] - s[j] + s[j] - s[i] - s[j] + s[n]))
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    ans = float('inf')
    for i in range(1, n):
        for j in range(i + 1, n):
            x = s[i]
            y = s[j] - s[i]
            z = s[n] - s[j]
            ans = min(ans, max(x, y, z) - min(x, y, z))
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_sum = sum(a)
    a_cumsum = [0] * (n + 1)
    for i in range(n):
        a_cumsum[i + 1] = a_cumsum[i] + a[i]
    ans = 10 ** 18
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            x = a_cumsum[i + 1]
            y = a_cumsum[j + 1] - a_cumsum[i + 1]
            z = a_cumsum[n] - a_cumsum[j + 1]
            ans = min(ans, max(x, y, z) - min(x, y, z))
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i]+a[i])
    ans = 10**20
    for i in range(1,n-2):
        for j in range(i+1,n-1):
            ans = min(ans, abs(s[i] - s[0]-s[i]), abs(s[j] - s[i]-s[j]), abs(s[n] - s[j]-s[n]))
    print(ans)
    return

=======
Suggestion 6

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    cumsum = [0]
    for a in A:
        cumsum.append(cumsum[-1] + a)
    ans = float('inf')
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            P = cumsum[i]
            Q = cumsum[j] - cumsum[i]
            R = cumsum[n] - cumsum[j]
            S = cumsum[n] - cumsum[j]
            ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    S = sum(A)
    a = []
    for i in range(N-1):
        S -= 2*A[i]
        a.append(S)
    print(min(a))

solve()

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    s = sum(a)
    r = 10 ** 9
    s1 = 0
    for i in range(n - 1):
        s1 += a[i]
        s -= a[i]
        r = min(r, abs(s1 - s))

    print(r)

solve()

=======
Suggestion 9

def solution(n, a):
    s = sum(a)
    min_diff = 1e9
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                p = sum(a[:i])
                q = sum(a[i:j])
                r = sum(a[j:k])
                s = sum(a[k:])
                min_diff = min(min_diff, max(p, q, r, s) - min(p, q, r, s))
    return min_diff

=======
Suggestion 10

def calc_min_diff(arr):
    arr.sort()
    min_diff = 10**9
    for i in range(1, len(arr)-2):
        diff = abs(sum(arr[:i]) - sum(arr[i:]))
        if diff < min_diff:
            min_diff = diff
    return min_diff
