Synthesizing 10/10 solutions

=======
Suggestion 1

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    if target < arr[0]:
        return 0
    if target > arr[right]:
        return right + 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1

    return left

=======
Suggestion 2

def get_nearest(arr, num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if num == arr[mid]:
            return num
        elif num < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    if right < 0:
        return arr[left]
    elif left > len(arr) - 1:
        return arr[right]

    if abs(num - arr[left]) < abs(num - arr[right]):
        return arr[left]
    else:
        return arr[right]

A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]
X = [int(input()) for _ in range(Q)]

for x in X:
    s = get_nearest(S, x)
    t = get_nearest(T, x)
    ans = min(abs(x - s), abs(x - t))
    ans = min(ans, abs(s - t) + min(abs(s - x), abs(t - x)))
    print(ans)

=======
Suggestion 3

def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for i in range(A)]
    T = [int(input()) for i in range(B)]
    X = [int(input()) for i in range(Q)]
    for x in X:
        s = 0
        t = 0
        while s < A and S[s] < x:
            s += 1
        while t < B and T[t] < x:
            t += 1
        ans = 10**11
        for s1 in [s-1, s]:
            for t1 in [t-1, t]:
                if s1 < 0 or s1 >= A or t1 < 0 or t1 >= B:
                    continue
                d1 = abs(S[s1] - x) + abs(T[t1] - S[s1])
                d2 = abs(T[t1] - x) + abs(S[s1] - T[t1])
                ans = min(ans, d1, d2)
        print(ans)

=======
Suggestion 4

def main():
    a,b,q = map(int,input().split())
    s = [0] * (a+2)
    s[0] = -float('inf')
    s[-1] = float('inf')
    for i in range(1,a+1):
        s[i] = int(input())
    t = [0] * (b+2)
    t[0] = -float('inf')
    t[-1] = float('inf')
    for i in range(1,b+1):
        t[i] = int(input())
    x = [0] * q
    for i in range(q):
        x[i] = int(input())
    for i in range(q):
        for j in range(a+1):
            if s[j] <= x[i] < s[j+1]:
                a1 = x[i] - s[j]
                a2 = s[j+1] - x[i]
                break
        for j in range(b+1):
            if t[j] <= x[i] < t[j+1]:
                b1 = x[i] - t[j]
                b2 = t[j+1] - x[i]
                break
        print(min(max(a1,b1),max(a2,b2),a1*2+b2,b1*2+a2))

=======
Suggestion 5

def binary_search(array, num):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == num:
            return mid
        elif array[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return left

=======
Suggestion 6

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
    for i in range(Q):
        #print("x[i] = ",x[i])
        #print("s = ",s)
        #print("t = ",t)
        #print("x[i] = ",x[i])
        s.append(x[i])
        t.append(x[i])
        s.sort()
        t.sort()
        #print("s = ",s)
        #print("t = ",t)
        #print("x[i] = ",x[i])
        s_index = s.index(x[i])
        t_index = t.index(x[i])
        #print("s_index = ",s_index)
        #print("t_index = ",t_index)
        #print("s[s_index-1] = ",s[s_index-1])
        #print("t[t_index-1] = ",t[t_index-1])
        #print("s[s_index] = ",s[s_index])
        #print("t[t_index] = ",t[t_index])
        #print("s[s_index+1] = ",s[s_index+1])
        #print("t[t_index+1] = ",t[t_index+1])
        s_minus = 0
        t_minus = 0
        s_plus = 0
        t_plus = 0
        if s_index > 0:
            s_minus = s[s_index-1]
        if t_index > 0:
            t_minus = t[t_index-1]
        if s_index < A:
            s_plus = s[s_index+1]
        if t_index < B:
            t_plus = t[t_index+1]
        #print("s_minus = ",s_minus)
        #print("t_minus = ",t_minus)
        #print("s_plus = ",s_plus)
        #print("t_plus = ",t_plus)
        s_minus_t_minus = abs(s_minus-t_minus)
        s_minus_t = abs(s_minus-x[i])
        s_minus_t_plus = abs(s_minus-t_plus)
        s

=======
Suggestion 7

def calc_dist(x, s, t):
    if x < s:
        return s - x
    elif t < x:
        return x - t
    else:
        return min(x - s, t - x) * 2 + max(x - s, t - x)

A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]

for _ in range(Q):
    x = int(input())
    s = 0
    t = 0

    while s < A and S[s] < x:
        s += 1
    while t < B and T[t] < x:
        t += 1

    ans = float('inf')
    for Ss in [S[s - 1]] if s > 0 else [float('inf')] + [S[s]] if s < A else [float('inf')] * 2:
        for Tt in [T[t - 1]] if t > 0 else [float('inf')] + [T[t]] if t < B else [float('inf')] * 2:
            ans = min(ans, calc_dist(x, Ss, Tt))

    print(ans)

=======
Suggestion 8

def solve():
    #入力
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]

    #番兵
    S = [-10**11] + S + [10**11]
    T = [-10**11] + T + [10**11]

    #二分探索
    from bisect import bisect_left, bisect_right
    for x in X:
        s = bisect_left(S, x)
        t = bisect_left(T, x)
        ans = 10**18
        for ss in [S[s-1], S[s]]:
            for tt in [T[t-1], T[t]]:
                #print(ss,tt)
                d1 = abs(ss-x) + abs(tt-ss)
                d2 = abs(tt-x) + abs(ss-tt)
                d3 = abs(ss-tt) + abs(x-tt)
                d4 = abs(tt-ss) + abs(x-ss)
                ans = min(ans, d1, d2, d3, d4)
        print(ans)

=======
Suggestion 9

def main():
    import sys
    from bisect import bisect_left, bisect_right
    input = sys.stdin.readline

    A, B, Q = map(int, input().split())
    s = [-float('inf')] + [int(input()) for _ in range(A)] + [float('inf')]
    t = [-float('inf')] + [int(input()) for _ in range(B)] + [float('inf')]
    x = [int(input()) for _ in range(Q)]

    for i in range(Q):
        ans = float('inf')
        for j in [bisect_left(s, x[i]), bisect_right(s, x[i])]:
            for k in [bisect_left(t, s[j]), bisect_right(t, s[j])]:
                ans = min(ans, abs(x[i] - s[j]) + abs(s[j] - t[k]))
            for k in [bisect_left(t, s[j - 1]), bisect_right(t, s[j - 1])]:
                ans = min(ans, abs(x[i] - s[j - 1]) + abs(s[j - 1] - t[k]))
        for j in [bisect_left(t, x[i]), bisect_right(t, x[i])]:
            for k in [bisect_left(s, t[j]), bisect_right(s, t[j])]:
                ans = min(ans, abs(x[i] - t[j]) + abs(t[j] - s[k]))
            for k in [bisect_left(s, t[j - 1]), bisect_right(s, t[j - 1])]:
                ans = min(ans, abs(x[i] - t[j - 1]) + abs(t[j - 1] - s[k]))
        print(ans)

=======
Suggestion 10

def binary_search(a, x):
    l = 0
    r = len(a)
    while l < r:
        m = (l + r) // 2
        if x < a[m]:
            r = m
        else:
            l = m + 1
    return l

a, b, q = map(int, input().split())
s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]
x = [int(input()) for _ in range(q)]

for i in range(q):
    ans = 10**18
    sr = binary_search(s, x[i])
    tr = binary_search(t, x[i])
    for si in (sr-1, sr):
        for ti in (tr-1, tr):
            d1 = abs(s[si] - x[i]) + abs(t[ti] - s[si])
            d2 = abs(t[ti] - x[i]) + abs(s[si] - t[ti])
            ans = min(ans, d1, d2)
    print(ans)
