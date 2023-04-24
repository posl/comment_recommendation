Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    for x in X:
        s = bisect.bisect_left(S, x)
        t = bisect.bisect_left(T, x)
        ans = float('inf')
        for s1 in [S[s-1], S[s]]:
            for t1 in [T[t-1], T[t]]:
                d1 = abs(s1 - x) + abs(t1 - s1)
                d2 = abs(t1 - x) + abs(s1 - t1)
                ans = min(ans, d1, d2)
        print(ans)

=======
Suggestion 2

def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]

    for x in X:
        s1 = 0
        s2 = 0
        t1 = 0
        t2 = 0
        for s in S:
            if s < x:
                s1 = s
            elif s == x:
                s1 = s
                s2 = s
                break
            else:
                s2 = s
                break
        for t in T:
            if t < x:
                t1 = t
            elif t == x:
                t1 = t
                t2 = t
                break
            else:
                t2 = t
                break

        s1_t1 = abs(x-s1) + abs(t1-s1)
        s1_t2 = abs(x-s1) + abs(t2-s1)
        s2_t1 = abs(x-s2) + abs(t1-s2)
        s2_t2 = abs(x-s2) + abs(t2-s2)
        s1_t1_s2_t1 = max(s1_t1, s2_t1)
        s1_t1_s2_t2 = max(s1_t1, s2_t2)
        s1_t2_s2_t1 = max(s1_t2, s2_t1)
        s1_t2_s2_t2 = max(s1_t2, s2_t2)
        print(min(s1_t1_s2_t1, s1_t1_s2_t2, s1_t2_s2_t1, s1_t2_s2_t2))

=======
Suggestion 3

def main():
    A,B,Q = map(int,input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    #print(A,B,Q)
    #print(s)
    #print(t)
    #print(x)
    
    import bisect
    INF = 10**11
    s.append(INF)
    s.insert(0,-INF)
    t.append(INF)
    t.insert(0,-INF)
    #print(s)
    #print(t)
    for i in range(Q):
        ans = INF
        now = x[i]
        s_idx = bisect.bisect_left(s,now)
        t_idx = bisect.bisect_left(t,now)
        for j in range(2):
            for k in range(2):
                d1 = abs(now-s[s_idx-j])+abs(s[s_idx-j]-t[t_idx-k])
                d2 = abs(now-t[t_idx-k])+abs(t[t_idx-k]-s[s_idx-j])
                ans = min(ans,d1,d2)
        print(ans)

=======
Suggestion 4

def main():
    a,b,q = map(int, input().split())
    s = [int(input()) for _ in range(a)]
    t = [int(input()) for _ in range(b)]
    x = [int(input()) for _ in range(q)]

    for i in range(q):
        ans = 10**18
        for j in range(a):
            for k in range(b):
                d = abs(x[i] - s[j])
                d += abs(s[j] - t[k])
                if d < ans:
                    ans = d
                d = abs(x[i] - t[k])
                d += abs(t[k] - s[j])
                if d < ans:
                    ans = d
        print(ans)

=======
Suggestion 5

def main():
    A,B,Q = map(int,input().split())
    s = []
    t = []
    x = []
    for i in range(A):
        s.append(int(input()))
    for i in range(B):
        t.append(int(input()))
    for i in range(Q):
        x.append(int(input()))

    for i in range(Q):
        ans = 10**10
        for j in range(A):
            for k in range(B):
                if s[j] <= x[i] <= t[k]:
                    ans = min(ans, max(x[i] - s[j], t[k] - x[i]) + t[k] - s[j])
                elif x[i] < s[j]:
                    ans = min(ans, s[j] - x[i] + t[k] - s[j])
                elif t[k] < x[i]:
                    ans = min(ans, x[i] - t[k] + t[k] - s[j])
        print(ans)

=======
Suggestion 6

def main():
    import bisect
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    s.append(float('inf'))
    t.append(float('inf'))
    for i in range(Q):
        ans = float('inf')
        d = x[i]
        j = bisect.bisect_right(s, d)
        k = bisect.bisect_right(t, d)
        for a in [s[j-1], s[j]]:
            for b in [t[k-1], t[k]]:
                ans = min(ans, abs(d-a)+abs(a-b), abs(d-b)+abs(b-a))
        print(ans)

=======
Suggestion 7

def binary_search(array, target):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid, target
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left, array[left]

A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
x = [int(input()) for _ in range(Q)]

for i in range(Q):
    idx_s, val_s = binary_search(s, x[i])
    idx_t, val_t = binary_search(t, x[i])
    if idx_s == 0:
        if idx_t == 0:
            print(max(val_s, val_t) - x[i])
        else:
            print(max(val_s, val_t) - min(val_t, x[i]))
    elif idx_t == 0:
        print(max(val_s, val_t) - min(val_s, x[i]))
    else:
        print(max(val_s, val_t) - max(min(val_s, x[i]), min(val_t, x[i])))

=======
Suggestion 8

def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    from bisect import bisect_left, bisect_right
    from itertools import accumulate
    from operator import itemgetter
    INF = float('inf')

    A, B, Q = map(int, readline().split())
    S = [int(readline()) for _ in range(A)]
    T = [int(readline()) for _ in range(B)]
    X = [int(readline()) for _ in range(Q)]

    for x in X:
        s = bisect_left(S, x)
        t = bisect_left(T, x)
        res = INF
        for ss in [S[s-1], S[s]] if s > 0 else [S[s]]:
            for tt in [T[t-1], T[t]] if t > 0 else [T[t]]:
                res = min(res, abs(ss - x) + abs(ss - tt), abs(tt - x) + abs(ss - tt))
        print(res)

=======
Suggestion 9

def binary_search(arr, target):
    index = 0
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            index = mid
            break
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        index = left
    return index

=======
Suggestion 10

def calc_dist(x, s, t):
    if x < s:
        return s - x
    elif t < x:
        return x - t
    else:
        return 0
