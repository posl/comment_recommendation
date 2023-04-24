Synthesizing 10/10 solutions

=======
Suggestion 1

def bisect_left(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo

=======
Suggestion 2

def main():
    A, B, Q = map(int, input().split())
    s = [-float('inf')] + [int(input()) for _ in range(A)] + [float('inf')]
    t = [-float('inf')] + [int(input()) for _ in range(B)] + [float('inf')]
    x = [int(input()) for _ in range(Q)]
    for i in range(Q):
        si = bisect.bisect_left(s, x[i])
        ti = bisect.bisect_left(t, x[i])
        ans = float('inf')
        for j in range(si-1, si+1):
            for k in range(ti-1, ti+1):
                ans = min(ans, abs(s[j]-x[i])+abs(t[k]-s[j]))
                ans = min(ans, abs(t[k]-x[i])+abs(s[j]-t[k]))
        print(ans)

=======
Suggestion 3

def main():
    A, B, Q = map(int, input().split())
    s = [-10**10] + [int(input()) for _ in range(A)] + [10**10]
    t = [-10**10] + [int(input()) for _ in range(B)] + [10**10]
    x = [int(input()) for _ in range(Q)]
    for i in range(Q):
        s_idx = bisect_left(s, x[i])
        t_idx = bisect_left(t, x[i])
        ans = 10**20
        for s_i in [s[s_idx-1], s[s_idx]]:
            for t_i in [t[t_idx-1], t[t_idx]]:
                ans = min(ans, max(s_i, t_i) - x[i])
                ans = min(ans, x[i] - min(s_i, t_i))
        print(ans)

=======
Suggestion 4

def main():
    A, B, Q = map(int, input().split())
    s = [-10**20] + [int(input()) for _ in range(A)] + [10**20]
    t = [-10**20] + [int(input()) for _ in range(B)] + [10**20]
    x = [int(input()) for _ in range(Q)]
    for xi in x:
        si = bisect.bisect_right(s, xi)
        ti = bisect.bisect_right(t, xi)
        ans = 10**20
        for sj in [si-1, si]:
            for tj in [ti-1, ti]:
                ans = min(ans, max(s[sj], t[tj]) - xi)
                ans = min(ans, xi - min(s[sj], t[tj]))
                ans = min(ans, abs(s[sj] - t[tj]) + min(abs(s[sj] - xi), abs(t[tj] - xi)))
        print(ans)

=======
Suggestion 5

def main():
    A, B, Q = map(int, input().split())
    s = [-10**20] + [int(input()) for _ in range(A)] + [10**20]
    t = [-10**20] + [int(input()) for _ in range(B)] + [10**20]
    x = [int(input()) for _ in range(Q)]
    for i in range(Q):
        ans = 10**20
        for j in range(A+2):
            for k in range(B+2):
                if s[j] <= x[i] and x[i] <= t[k]:
                    ans = min(ans, max(x[i]-s[j], t[k]-x[i]))
                elif s[j] > x[i] and t[k] < x[i]:
                    ans = min(ans, min(x[i]-s[j], t[k]-x[i]), 2*(x[i]-s[j])+t[k]-s[j], 2*(t[k]-x[i])+t[k]-s[j])
                elif s[j] > x[i]:
                    ans = min(ans, s[j]-x[i], t[k]-s[j]+x[i]-s[j])
                elif t[k] < x[i]:
                    ans = min(ans, x[i]-t[k], t[k]-s[j]+t[k]-x[i])
        print(ans)

=======
Suggestion 6

def main():
    A, B, Q = map(int, input().split())
    s = [-10**15] + [int(input()) for _ in range(A)] + [10**15]
    t = [-10**15] + [int(input()) for _ in range(B)] + [10**15]
    x = [int(input()) for _ in range(Q)]
    for i in x:
        s1, s2 = get_lr(s, i)
        t1, t2 = get_lr(t, i)
        ans = min(
            max(i - s1, t2 - i),
            max(i - s2, t1 - i),
            max(i - s1, t1 - i) + min(i - s1, t1 - i),
            max(i - s2, t2 - i) + min(i - s2, t2 - i),
            max(i - s1, t2 - i) + min(i - s1, t2 - i),
            max(i - s2, t1 - i) + min(i - s2, t1 - i),
        )
        print(ans)

=======
Suggestion 7

def main():
    A, B, Q = map(int, input().split())
    s = [-10**15] + [int(input()) for i in range(A)] + [10**15]
    t = [-10**15] + [int(input()) for i in range(B)] + [10**15]
    x = [int(input()) for i in range(Q)]
    for i in x:
        ans = 10**15
        for j in s:
            if i <= j:
                ans = min(ans, j - i + min(abs(j - k) for k in t))
            else:
                ans = min(ans, i - j + min(abs(j - k) for k in t))
        print(ans)

main()

=======
Suggestion 8

def solve():
    A, B, Q = map(int, input().split())
    S = [-10**20] + [int(input()) for _ in range(A)] + [10**20]
    T = [-10**20] + [int(input()) for _ in range(B)] + [10**20]
    X = [int(input()) for _ in range(Q)]

    ans = []
    for x in X:
        s = bisect.bisect_right(S, x)
        t = bisect.bisect_right(T, x)
        ans.append(min(
            max(S[s - 1], T[t - 1]) - x,
            x - min(S[s], T[t]),
            S[s] - T[t - 1] + min(S[s] - x, x - T[t - 1]),
            T[t] - S[s - 1] + min(T[t] - x, x - S[s - 1]),
        ))
    print('

'.join(map(str, ans)))

=======
Suggestion 9

def lower_bound(a, x):
    ok = -1
    ng = len(a)
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if a[mid] < x:
            ok = mid
        else:
            ng = mid
    return ng

=======
Suggestion 10

def main():
    import bisect
    import sys
    input = sys.stdin.readline
    A, B, Q = map(int, input().split())
    S = [-10**10] + [int(input()) for _ in range(A)] + [10**10]
    T = [-10**10] + [int(input()) for _ in range(B)] + [10**10]
    X = [int(input()) for _ in range(Q)]
    for x in X:
        i = bisect.bisect_right(S, x)
        j = bisect.bisect_right(T, x)
        ans = 10**20
        for s in S[i-1:i+1]:
            for t in T[j-1:j+1]:
                ans = min(ans, max(s-x, x-t), max(t-x, x-s))
        print(ans)
