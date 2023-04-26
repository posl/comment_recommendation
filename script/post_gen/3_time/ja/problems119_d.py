Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    s.insert(0, -10**11)
    s.append(10**11)
    t.insert(0, -10**11)
    t.append(10**11)
    for i in range(Q):
        left = 0
        right = 0
        for j in range(A+1):
            if x[i] >= s[j]:
                left = s[j]
            else:
                break
        for j in range(B+1):
            if x[i] >= t[j]:
                right = t[j]
            else:
                break
        ans = min(abs(x[i]-left)+abs(left-right), abs(x[i]-right)+abs(left-right), abs(x[i]-left)+abs(left-right))
        print(ans)

=======
Suggestion 2

def main():
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    s.append(10 ** 11)
    t.append(10 ** 11)
    for i in range(Q):
        ans = 10 ** 20
        a = bisect_left(s, x[i])
        b = bisect_left(t, x[i])
        for j in (a - 1, a):
            for k in (b - 1, b):
                d1 = abs(s[j] - x[i]) + abs(t[k] - s[j])
                d2 = abs(t[k] - x[i]) + abs(s[j] - t[k])
                ans = min(ans, d1, d2)
        print(ans)

=======
Suggestion 3

def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    S = [float('-inf')] + S + [float('inf')]
    T = [float('-inf')] + T + [float('inf')]
    from bisect import bisect_left, bisect_right
    for x in X:
        s = bisect_right(S, x)
        t = bisect_right(T, x)
        ans = float('inf')
        for s1 in [S[s-1], S[s]]:
            for t1 in [T[t-1], T[t]]:
                ans = min(ans, abs(x-s1)+abs(s1-t1), abs(x-t1)+abs(t1-s1))
        print(ans)

=======
Suggestion 4

def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]

    for i in range(Q):
        x = X[i]
        s = bisect_left(S, x)
        t = bisect_left(T, x)
        ans = 10**20
        for ss in (S[max(0, s-1)], S[min(A-1, s)]):
            for tt in (T[max(0, t-1)], T[min(B-1, t)]):
                d1 = abs(ss - x) + abs(tt - ss)
                d2 = abs(tt - x) + abs(ss - tt)
                ans = min(ans, d1, d2)
        print(ans)

=======
Suggestion 5

def main():
    A,B,Q = map(int,input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]

    for x in X:
        if x < S[0]:
            print(S[0]-x+min(S[0]-x,T[0]-S[0]))
        elif x > T[-1]:
            print(x-T[-1]+min(x-T[-1],T[-1]-S[-1]))
        else:
            l = 0
            r = A-1
            while r-l > 1:
                m = (l+r)//2
                if S[m] >= x:
                    r = m
                else:
                    l = m
            s = r
            l = 0
            r = B-1
            while r-l > 1:
                m = (l+r)//2
                if T[m] >= x:
                    r = m
                else:
                    l = m
            t = r
            ans = min(S[s]-x,T[t]-x)
            ans += min(S[s]-x,x-T[t])
            ans += min(x-S[s],T[t]-x)
            ans += min(x-S[s],x-T[t])
            print(ans)

=======
Suggestion 6

def main():
    A, B, Q = map(int, input().split())
    s = [0]*A
    t = [0]*B
    x = [0]*Q
    for i in range(A):
        s[i] = int(input())
    for i in range(B):
        t[i] = int(input())
    for i in range(Q):
        x[i] = int(input())
    for i in range(Q):
        ans = 0
        for j in range(A):
            if x[i] < s[j]:
                if j == 0:
                    ans += s[j] - x[i]
                else:
                    if x[i] - s[j-1] < s[j] - x[i]:
                        ans += x[i] - s[j-1]
                    else:
                        ans += s[j] - x[i]
                break
            elif j == A-1:
                ans += x[i] - s[j]
        for j in range(B):
            if x[i] < t[j]:
                if j == 0:
                    ans += t[j] - x[i]
                else:
                    if x[i] - t[j-1] < t[j] - x[i]:
                        ans += x[i] - t[j-1]
                    else:
                        ans += t[j] - x[i]
                break
            elif j == B-1:
                ans += x[i] - t[j]
        print(ans)

=======
Suggestion 7

def solve():
    import sys
    input = sys.stdin.readline
    A,B,Q = map(int,input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    s = [-float("inf")]+s+[float("inf")]
    t = [-float("inf")]+t+[float("inf")]
    from bisect import bisect_left,bisect_right
    def f(x):
        i = bisect_left(s,x)
        j = bisect_left(t,x)
        return min(
            max(s[i],t[j])-x,
            x-min(s[i-1],t[j-1]),
            s[i]-t[j-1]+min(s[i]-x,x-t[j-1]),
            t[j]-s[i-1]+min(t[j]-x,x-s[i-1])
        )
    print(*map(f,x),sep="\n")

solve()

=======
Suggestion 8

def binary_search(list, target):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

a, b, q = map(int, input().split())
s = [int(input()) for i in range(a)]
t = [int(input()) for i in range(b)]
x = [int(input()) for i in range(q)]

for i in range(q):
    ans = 10**18
    s_index = binary_search(s, x[i])
    t_index = binary_search(t, x[i])
    for ss in [s[s_index - 1], s[s_index]]:
        for tt in [t[t_index - 1], t[t_index]]:
            d1 = abs(ss - x[i]) + abs(tt - ss)
            d2 = abs(tt - x[i]) + abs(ss - tt)
            ans = min(ans, d1, d2)
    print(ans)

=======
Suggestion 9

def find_nearest(arr, num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return arr[mid]
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return arr[right]

A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
x = [int(input()) for _ in range(Q)]

for i in range(Q):
    ans = 10 ** 20
    near_s = find_nearest(s, x[i])
    near_t = find_nearest(t, x[i])
    ans = min(ans, abs(near_s - x[i]) + abs(near_t - near_s))
    ans = min(ans, abs(near_t - x[i]) + abs(near_s - near_t))
    print(ans)

=======
Suggestion 10

def main():
    pass
