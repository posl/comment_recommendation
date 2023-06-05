Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(A, B, Q, s, t, x):
    import bisect
    INF = 10**11
    s = [0] + s + [INF]
    t = [0] + t + [INF]
    for _ in range(Q):
        ans = INF
        xi = x[_]
        s_i = bisect.bisect_right(s, xi)
        t_i = bisect.bisect_right(t, xi)
        for si in [s[s_i-1], s[s_i]]:
            for ti in [t[t_i-1], t[t_i]]:
                d1 = abs(si - xi) + abs(ti - si)
                d2 = abs(ti - xi) + abs(si - ti)
                ans = min(ans, d1, d2)
        print(ans)

=======
Suggestion 2

def get_min_dist(x, s, t):
    s_len = len(s)
    t_len = len(t)
    s_index = 0
    t_index = 0
    min_dist = 2**32
    while s_index < s_len and t_index < t_len:
        dist = abs(s[s_index] - x) + abs(t[t_index] - s[s_index])
        if dist < min_dist:
            min_dist = dist
        if s[s_index] < t[t_index]:
            s_index += 1
        else:
            t_index += 1
    while s_index < s_len:
        dist = abs(s[s_index] - x) + abs(t[-1] - s[s_index])
        if dist < min_dist:
            min_dist = dist
        s_index += 1
    while t_index < t_len:
        dist = abs(s[-1] - x) + abs(t[t_index] - s[-1])
        if dist < min_dist:
            min_dist = dist
        t_index += 1
    return min_dist

=======
Suggestion 3

def solve():
    # 1. 读取输入
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]

    # 2. 为了计算方便，将所有的值都加上一个哨兵，使得所有的值都是正数
    s = [float('-inf')] + s + [float('inf')]
    t = [float('-inf')] + t + [float('inf')]

    # 3. 对于每一个查询，找到最近的神社和寺庙
    # 3.1. 对于每一个查询，找到最近的神社和寺庙
    for i in range(Q):
        # 3.1.1. 二分查找最近的神社
        left, right = 0, A + 1
        while left < right:
            mid = (left + right) // 2
            if s[mid] > x[i]:
                right = mid
            else:
                left = mid + 1
        # left - 1就是最近的神社
        shrine = s[left - 1]

        # 3.1.2. 二分查找最近的寺庙
        left, right = 0, B + 1
        while left < right:
            mid = (left + right) // 2
            if t[mid] > x[i]:
                right = mid
            else:
                left = mid + 1
        # left - 1就是最近的寺庙
        temple = t[left - 1]

        # 3.1.3. 计算最近的神社和寺庙之间的距离
        dist1 = abs(shrine - x[i])
        dist2 = abs(temple - x[i])
        dist3 = abs(shrine - temple) + min(dist1, dist2)

        # 3.1.4. 打印答案
        print(min(dist1, dist2, dist3))

if

=======
Suggestion 4

def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return left

A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
x = [int(input()) for _ in range(Q)]

for i in range(Q):
    index_s = binary_search(s, x[i])
    index_t = binary_search(t, x[i])
    ans = 10 ** 11
    for j in [index_s - 1, index_s]:
        for k in [index_t - 1, index_t]:
            d1 = abs(s[j] - x[i]) + abs(t[k] - s[j])
            d2 = abs(t[k] - x[i]) + abs(s[j] - t[k])
            ans = min(ans, d1, d2)
    print(ans)

=======
Suggestion 5

def main():
    a,b,q=map(int,input().split())
    s=[int(input()) for _ in range(a)]
    t=[int(input()) for _ in range(b)]
    x=[int(input()) for _ in range(q)]
    for i in range(q):
        ans=10**11
        for j in range(a):
            for k in range(b):
                if s[j]<=x[i]<=t[k]:
                    ans=min(ans,min(x[i]-s[j],t[k]-x[i])+t[k]-s[j])
                elif x[i]<s[j]:
                    ans=min(ans,s[j]-x[i])
                else:
                    ans=min(ans,x[i]-t[k])
        print(ans)

=======
Suggestion 6

def solve():
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
        ans = 10000000000000000000
        for j in range(A):
            for k in range(B):
                temp = max(s[j],t[k])-min(s[j],t[k])
                temp += min(max(s[j],x[i]),max(x[i],t[k]))-min(max(s[j],x[i]),max(x[i],t[k]))
                temp = min(temp,max(max(s[j],x[i]),max(x[i],t[k]))-min(max(s[j],x[i]),max(x[i],t[k])))
                ans = min(ans,temp)
        print(ans)

=======
Suggestion 7

def main():
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    inf = 10 ** 18
    s = [-inf] + s + [inf]
    t = [-inf] + t + [inf]
    import bisect
    for i in x:
        si = bisect.bisect_left(s, i)
        ti = bisect.bisect_left(t, i)
        ans = inf
        for ss in [s[si - 1], s[si]]:
            for tt in [t[ti - 1], t[ti]]:
                d = min(abs(i - ss), abs(i - tt))
                d += abs(ss - tt)
                ans = min(ans, d)
        print(ans)

=======
Suggestion 8

def find_nearest(array, value):
    if value < array[0]:
        return array[0]
    elif value > array[len(array)-1]:
        return array[len(array)-1]
    else:
        for i in range(len(array)):
            if array[i] >= value:
                if array[i] - value > value - array[i-1]:
                    return array[i-1]
                else:
                    return array[i]

=======
Suggestion 9

def solve():
    pass

=======
Suggestion 10

def binary_search(list1, x):
    left = 0
    right = len(list1) - 1
    while left <= right:
        mid = (left + right) // 2
        if list1[mid] == x:
            return mid
        elif list1[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left


A, B, Q = map(int, input().split())
s = [int(input()) for i in range(A)]
t = [int(input()) for i in range(B)]
x = [int(input()) for i in range(Q)]

for i in range(Q):
    s_index = binary_search(s, x[i])
    t_index = binary_search(t, x[i])
    if s_index == 0:
        s_left = 0
    else:
        s_left = s[s_index - 1]
    if t_index == 0:
        t_left = 0
    else:
        t_left = t[t_index - 1]
    if s_index == A:
        s_right = 10 ** 10
    else:
        s_right = s[s_index]
    if t_index == B:
        t_right = 10 ** 10
    else:
        t_right = t[t_index]
    ans = 10 ** 10
    ans = min(ans, abs(x[i] - s_left) + abs(s_left - t_left))
    ans = min(ans, abs(x[i] - s_left) + abs(s_left - t_right))
    ans = min(ans, abs(x[i] - s_right) + abs(s_right - t_left))
    ans = min(ans, abs(x[i] - s_right) + abs(s_right - t_right))
    ans = min(ans, abs(x[i] - t_left) + abs(t_left - s_left))
    ans = min(ans, abs(x[i] - t_left) + abs(t_left - s_right))
    ans = min(ans, abs(x[i] - t_right) + abs(t_right - s_left))
    ans = min(ans, abs(x[i] - t_right) + abs(t_right - s_right))
    print(ans)
