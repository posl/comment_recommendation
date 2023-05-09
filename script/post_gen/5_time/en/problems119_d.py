Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    for i in range(Q):
        l = 0
        r = 0
        while l < A and s[l] < x[i]:
            l += 1
        while r < B and t[r] < x[i]:
            r += 1
        if l == A and r == B:
            print(min(abs(s[-1] - x[i]), abs(t[-1] - x[i])))
        elif l == A:
            print(min(abs(s[-1] - x[i]), abs(t[r] - x[i]), abs(t[r] - x[i]) + abs(t[r] - s[-1])))
        elif r == B:
            print(min(abs(t[-1] - x[i]), abs(s[l] - x[i]), abs(s[l] - x[i]) + abs(s[l] - t[-1])))
        else:
            print(min(abs(s[l] - x[i]), abs(t[r] - x[i]), abs(s[l] - x[i]) + abs(s[l] - t[r]), abs(t[r] - x[i]) + abs(s[l] - t[r])))

=======
Suggestion 2

def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]

    for x in X:
        s1 = s2 = t1 = t2 = 0
        for i in range(A):
            if S[i] <= x:
                s1 = S[i]
            else:
                s2 = S[i]
                break
        for i in range(B):
            if T[i] <= x:
                t1 = T[i]
            else:
                t2 = T[i]
                break

        ans = []
        ans.append(max(x - s1, x - t1))
        ans.append(max(s2 - x, t2 - x))
        ans.append(2 * (x - s1) + (t2 - x))
        ans.append(2 * (t1 - x) + (x - s2))
        ans.append((s2 - x) + (x - t1))
        ans.append((t2 - x) + (x - s1))

        print(min(ans))

=======
Suggestion 3

def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    S = [-10**11] + S + [10**11]
    T = [-10**11] + T + [10**11]
    from bisect import bisect_left, bisect_right
    def solve(x):
        s = bisect_left(S, x)
        t = bisect_left(T, x)
        res = 10**11
        for s0 in [S[s-1], S[s]]:
            for t0 in [T[t-1], T[t]]:
                d1 = abs(x-s0) + abs(s0-t0)
                d2 = abs(x-t0) + abs(t0-s0)
                res = min(res, d1, d2)
        return res
    for x in X:
        print(solve(x))

=======
Suggestion 4

def main():
    A, B, Q = map(int, input().split())
    s = [0] * (A + 2)
    t = [0] * (B + 2)
    x = [0] * Q
    for i in range(A):
        s[i + 1] = int(input())
    for i in range(B):
        t[i + 1] = int(input())
    s[A + 1] = 10 ** 11
    t[B + 1] = 10 ** 11
    for i in range(Q):
        x[i] = int(input())
    for i in range(Q):
        j = 1
        k = 1
        while x[i] > s[j] and j <= A:
            j += 1
        while x[i] > t[k] and k <= B:
            k += 1
        ans = 10 ** 11
        for l in range(2):
            for m in range(2):
                d1 = abs(x[i] - s[j - 1 + l]) + abs(s[j - 1 + l] - t[k - 1 + m])
                d2 = abs(x[i] - t[k - 1 + m]) + abs(t[k - 1 + m] - s[j - 1 + l])
                ans = min(ans, d1, d2)
        print(ans)

=======
Suggestion 5

def main():
    A,B,Q = map(int,input().split())
    s = [0]*A
    t = [0]*B
    x = [0]*Q
    for i in range(A):
        s[i] = int(input())
    for i in range(B):
        t[i] = int(input())
    for i in range(Q):
        x[i] = int(input())
    s = [-float('inf')]+s+[float('inf')]
    t = [-float('inf')]+t+[float('inf')]
    for i in range(Q):
        l = bisect.bisect_left(s,x[i])
        r = bisect.bisect_left(t,x[i])
        ans = float('inf')
        for j in [s[l-1],s[l]]:
            for k in [t[r-1],t[r]]:
                d1 = abs(j-x[i])+abs(k-j)
                d2 = abs(k-x[i])+abs(j-k)
                ans = min(ans,d1,d2)
        print(ans)

=======
Suggestion 6

def solve(A, B, Q, s, t, x):
    s = [-float('inf')] + s + [float('inf')]
    t = [-float('inf')] + t + [float('inf')]
    from bisect import bisect_left
    for xi in x:
        si = bisect_left(s, xi)
        ti = bisect_left(t, xi)
        res = float('inf')
        for sj in [s[si - 1], s[si]]:
            for tk in [t[ti - 1], t[ti]]:
                d1 = abs(sj - xi) + abs(tk - sj)
                d2 = abs(tk - xi) + abs(tk - sj)
                res = min(res, d1, d2)
        print(res)

=======
Suggestion 7

def main():
    [A, B, Q] = [int(x) for x in input().rstrip().split()]
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]

    for x in X:
        sl = 0
        sr = 0
        tl = 0
        tr = 0

        while sl < A and S[sl] < x:
            sl += 1
        if sl > 0:
            sr = sl - 1
        else:
            sr = sl

        while tl < B and T[tl] < x:
            tl += 1
        if tl > 0:
            tr = tl - 1
        else:
            tr = tl

        ans = 10 ** 10

        for s in [S[sr], S[sl]]:
            for t in [T[tr], T[tl]]:
                ans = min(ans, abs(s - x) + abs(t - s))
                ans = min(ans, abs(t - x) + abs(s - t))

        print(ans)

main()

=======
Suggestion 8

def main():
    import bisect
    INF = 10**18
    A, B, Q = map(int, input().split())
    S = [-INF] + [int(input()) for _ in range(A)] + [INF]
    T = [-INF] + [int(input()) for _ in range(B)] + [INF]
    X = [int(input()) for _ in range(Q)]

    for x in X:
        s, t = bisect.bisect_left(S, x), bisect.bisect_left(T, x)
        ans = INF
        for s0 in [S[s-1], S[s]]:
            for t0 in [T[t-1], T[t]]:
                ans = min(ans, abs(s0 - x) + abs(s0 - t0), abs(t0 - x) + abs(s0 - t0))
        print(ans)

=======
Suggestion 9

def get_min_distance(shrines, temples, x):
    min_distance = float('inf')
    for shrine in shrines:
        for temple in temples:
            distance = abs(shrine - x) + abs(temple - shrine)
            if distance < min_distance:
                min_distance = distance
    return min_distance

=======
Suggestion 10

def get_nearest(array, value):
    if value <= array[0]:
        return array[0]
    if value >= array[-1]:
        return array[-1]
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == value:
            return array[mid]
        elif array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return array[high] if abs(array[high] - value) < abs(array[low] - value) else array[low]
