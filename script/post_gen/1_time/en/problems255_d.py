Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    s = sum(a)
    for i in range(q):
        print(s + x[i])

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    ans = 0
    for i in range(n-1):
        ans += abs(a[i]-a[i+1])
    for i in range(q):
        if i == 0:
            print(ans + abs(a[0]-x[i]) + abs(a[1]-x[i]))
        elif i == q-1:
            print(ans + abs(a[n-2]-x[i]) + abs(a[n-1]-x[i]))
        else:
            print(ans + abs(a[i-1]-x[i]) + abs(a[i+1]-x[i]) - abs(a[i-1]-a[i]) - abs(a[i]-a[i+1]))
        a[i] = x[i]

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]

    print(n, q)
    print(a)
    print(x)

    for i in range(q):
        print(x[i])

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]

    for i in range(n-1):
        a[i+1] += a[i]

    for i in range(q):
        ans = 0
        for j in range(n):
            ans += abs(a[j] - x[i])
        print(ans)

=======
Suggestion 5

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    a.sort()
    s = sum(a)
    for i in range(q):
        print(s + x[i] * n)

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    A.sort()
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])

    for x in X:
        l = 0
        r = N
        while r - l > 1:
            c = (l + r) // 2
            if A[c] < x:
                l = c
            else:
                r = c

        ans = 0
        ans += S[l]
        ans += (N - l) * x
        print(ans)

=======
Suggestion 7

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    X = [0] + X + [0]
    ans = 0
    for i in range(1, Q+2):
        ans += abs(X[i] - X[i-1])
        if i == 1:
            ans += abs(A[0] - X[i])
        elif i == Q+1:
            ans += abs(A[N-1] - X[i-1])
        else:
            ans += abs(A[i-2] - A[i-1])
            ans += abs(A[i-1] - X[i])
    print(ans)

=======
Suggestion 8

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]

    a.sort()
    a.append(10**20)

    b = [0]
    for i in range(1, n + 1):
        b.append(b[i - 1] + a[i] - a[i - 1])

    for i in range(q):
        l = 0
        r = n
        while r - l > 1:
            m = (l + r) // 2
            if a[m] < x[i]:
                l = m
            else:
                r = m
        print(b[l] + (n - l) * (x[i] - 1))

=======
Suggestion 9

def solve(n, q, a, x):
    a.sort()
    x.sort()
    ans = 0
    for i in range(q):
        ans += (x[i] - a[i]) if x[i] > a[i] else (a[i] - x[i])
    return ans

=======
Suggestion 10

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]

    # 1回の操作で最大でどれだけ変化するか
    max_change = max(a) - min(a)

    # xの最大値が変化する最大値を超えている場合は、xの最大値を最大値にする
    if max(x) > max_change:
        max_change = max(x)

    # aの最小値を引いたものが、xの最小値よりも大きい場合は、xの最小値を最小値にする
    if min(a) - min(x) > 0:
        min_change = min(x)
    else:
        min_change = min(a) - min(x)

    # xの最小値を引いたものが、aの最大値よりも小さい場合は、xの最大値を最大値にする
    if max(a) - max(x) < 0:
        max_change = max(x)

    # aの最小値を引いたものが、xの最大値よりも大きい場合は、xの最小値を最小値にする
    if min(a) - min(x) > 0:
        min_change = min(x)

    # aの最大値を引いたものが、xの最小値よりも小さい場合は、xの最大値を最大値にする
    if max(a) - max(x) < 0:
        max_change = max(x)

    # aの最小値を引いたものが、xの最大値よりも大きい場合は、xの最小値を最小値にする
    if min(a) - min(x) > 0:
        min_change = min(x)

    # aの最大値を引いたものが、xの最小値よりも小さい場合は、
