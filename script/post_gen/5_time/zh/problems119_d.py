Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, Q = [int(i) for i in input().split()]
    s = [int(input()) for i in range(A)]
    t = [int(input()) for i in range(B)]
    x = [int(input()) for i in range(Q)]
    s = [-float('inf')] + s + [float('inf')]
    t = [-float('inf')] + t + [float('inf')]
    import bisect
    for xi in x:
        si = bisect.bisect_left(s, xi)
        ti = bisect.bisect_left(t, xi)
        print(min(max(s[si], t[ti]) - xi, xi - min(s[si - 1], t[ti - 1]), 2 * (xi - s[si - 1]) + t[ti] - xi, 2 * (t[ti - 1] - xi) + xi - s[si]))

=======
Suggestion 2

def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
    return left

a, b, q = map(int, input().split())
s = [0] * a
t = [0] * b
x = [0] * q
for i in range(a):
    s[i] = int(input())
for i in range(b):
    t[i] = int(input())
for i in range(q):
    x[i] = int(input())
for i in range(q):
    s_index = binary_search(s, x[i])
    t_index = binary_search(t, x[i])
    min_distance = 10 ** 10
    for j in range(2):
        for k in range(2):
            distance = abs(s[s_index - j] - t[t_index - k]) + min(abs(x[i] - s[s_index - j]), abs(x[i] - t[t_index - k]))
            if distance < min_distance:
                min_distance = distance
    print(min_distance)

=======
Suggestion 3

def get_min_distance(s,t,x):
    if x < s[0]:
        return s[0] - x
    elif x > t[-1]:
        return x - t[-1]
    else:
        min_distance = float("inf")
        for i in range(len(s)):
            if x >= s[i] and x <= t[i]:
                return 0
            else:
                if abs(s[i] - x) < min_distance:
                    min_distance = abs(s[i] - x)
                if abs(t[i] - x) < min_distance:
                    min_distance = abs(t[i] - x)
        return min_distance

=======
Suggestion 4

def main():
    a,b,q = map(int,input().split())
    s = [0]*(a+2)
    t = [0]*(b+2)
    x = [0]*q
    for i in range(a):
        s[i+1] = int(input())
    for i in range(b):
        t[i+1] = int(input())
    for i in range(q):
        x[i] = int(input())
    s[0] = t[0] = -10**11
    s[a+1] = t[b+1] = 10**11
    for i in range(q):
        l = 0
        r = a+1
        while r-l > 1:
            m = (l+r)//2
            if s[m] <= x[i]:
                l = m
            else:
                r = m
        l1 = l
        r1 = l+1
        l = 0
        r = b+1
        while r-l > 1:
            m = (l+r)//2
            if t[m] <= x[i]:
                l = m
            else:
                r = m
        l2 = l
        r2 = l+1
        ans = 10**11
        for j in range(2):
            for k in range(2):
                d1 = abs(x[i]-s[l1+j])
                d2 = abs(s[r1-j]-x[i])
                d3 = abs(x[i]-t[l2+k])
                d4 = abs(t[r2-k]-x[i])
                ans = min(ans,max(d1,d2,d3,d4))
        print(ans)

=======
Suggestion 5

def binarySearch(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low

A, B, Q = [int(x) for x in input().split()]
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
x = [int(input()) for _ in range(Q)]
s.sort()
t.sort()

for i in range(Q):
    si = binarySearch(s, x[i])
    ti = binarySearch(t, x[i])
    ans = 10 ** 12
    for ss in [s[si - 1], s[si]]:
        for tt in [t[ti - 1], t[ti]]:
            d1 = abs(ss - x[i]) + abs(tt - ss)
            d2 = abs(tt - x[i]) + abs(ss - tt)
            ans = min(ans, d1, d2)
    print(ans)

=======
Suggestion 6

def solve():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    INF = 10 ** 18
    S = [-INF] + S + [INF]
    T = [-INF] + T + [INF]
    from bisect import bisect_left
    for _ in range(Q):
        x = int(input())
        ans = INF
        s = bisect_left(S, x)
        t = bisect_left(T, x)
        for S1 in [S[s - 1], S[s]]:
            for T1 in [T[t - 1], T[t]]:
                d1 = abs(S1 - x) + abs(T1 - S1)
                d2 = abs(T1 - x) + abs(S1 - T1)
                ans = min(ans, d1, d2)
        print(ans)

=======
Suggestion 7

def get_min_distance(s,t,x):
    result = 0
    if len(s) == 0:
        return t[0] - x
    if len(t) == 0:
        return x - s[-1]
    if len(s) == 1 and len(t) == 1:
        return min(t[0] - x, x - s[-1])
    if x in s or x in t:
        return 0
    if x < s[0]:
        return s[0] - x
    if x > t[-1]:
        return x - t[-1]
    if x > s[-1] and x < t[0]:
        return min(x - s[-1], t[0] - x)
    if x > s[-1]:
        return x - s[-1]
    if x < t[0]:
        return t[0] - x
    left = 0
    right = len(s) - 1
    while left < right:
        mid = (left + right) // 2
        if s[mid] < x:
            left = mid + 1
        else:
            right = mid
    left = 0
    right = len(t) - 1
    while left < right:
        mid = (left + right) // 2
        if t[mid] < x:
            left = mid + 1
        else:
            right = mid
    return min(x - s[left], t[right] - x)

=======
Suggestion 8

def getMinDistance(s,t,x):
    minDistance = float('inf')
    for i in range(len(s)):
        if s[i] <= x:
            for j in range(len(t)):
                if t[j] <= x:
                    if s[i] + t[j] < minDistance:
                        minDistance = s[i] + t[j]
    return minDistance

=======
Suggestion 9

def main():
    a,b,q = map(int,input().split())
    s = []
    t = []
    x = []
    for _ in range(a):
        s.append(int(input()))
    for _ in range(b):
        t.append(int(input()))
    for _ in range(q):
        x.append(int(input()))

    for i in range(q):
        s.append(x[i])
        t.append(x[i])
        s.sort()
        t.sort()
        index_s = s.index(x[i])
        index_t = t.index(x[i])
        if index_s == 0:
            print(abs(t[0]-x[i]))
        elif index_s == len(s)-1:
            print(abs(s[-1]-x[i]))
        else:
            if index_s <= index_t:
                print(min(abs(t[index_t]-x[i]),abs(s[index_s-1]-x[i])+abs(s[index_s-1]-t[index_t]),abs(s[index_s]-x[i])+abs(s[index_s]-t[index_t])))
            else:
                print(min(abs(s[index_s]-x[i]),abs(t[index_t-1]-x[i])+abs(t[index_t-1]-s[index_s]),abs(t[index_t]-x[i])+abs(t[index_t]-s[index_s])))

=======
Suggestion 10

def solve():
    # 读取输入
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]

    # 二分查找
    def binary_search(a, x):
        l = 0
        r = len(a) - 1
        while r - l > 1:
            m = (l + r) // 2
            if a[m] < x:
                l = m
            else:
                r = m
        return l, r

    # 计算最短距离
    def calc(a, b, x):
        l, r = binary_search(a, x)
        res = min(abs(x - a[l]) + abs(a[l] - b[l]),
                  abs(x - a[r]) + abs(a[r] - b[r]),
                  abs(x - b[l]) + abs(a[l] - b[l]),
                  abs(x - b[r]) + abs(a[r] - b[r]))
        return res

    # 计算答案
    for i in range(Q):
        res = min(calc(s, t, x[i]), calc(t, s, x[i]))
        print(res)
