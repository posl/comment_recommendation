Synthesizing 9/10 solutions

=======
Suggestion 1

def binSearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = int((left + right) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left

=======
Suggestion 2

def find_nearest(array, item):
    if item < array[0]:
        return array[0]
    if item > array[-1]:
        return array[-1]
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == item:
            return array[mid]
        elif array[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    if abs(array[low] - item) < abs(array[high] - item):
        return array[low]
    else:
        return array[high]

=======
Suggestion 3

def binary_search(s, t, x):
    # 二分查找
    # s, t: list, x: int
    if s[-1] <= x:
        return abs(t[0] - x)
    elif t[-1] <= x:
        return abs(s[0] - x)
    else:
        left = 0
        right = len(s) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if s[mid] < x:
                left = mid
            else:
                right = mid
        return min(abs(s[left] - x) + abs(t[0] - s[left]), abs(s[right] - x) + abs(t[0] - s[right]))

=======
Suggestion 4

def main():
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]

    for i in range(Q):
        ans = 10 ** 11
        for j in range(A):
            for k in range(B):
                ans = min(ans, abs(x[i] - s[j]) + abs(s[j] - t[k]))
                ans = min(ans, abs(x[i] - t[k]) + abs(t[k] - s[j]))
        print(ans)

=======
Suggestion 5

def solve(a, b, s, t, x):
    # 二分查找
    ans = 0
    for xi in x:
        # 向西走
        left = 0
        right = a
        while left < right:
            mid = (left + right) // 2
            if s[mid] < xi:
                left = mid + 1
            else:
                right = mid
        # 向东走
        s1 = abs(xi - s[left])
        s2 = abs(xi - s[left - 1]) if left > 0 else 10 ** 10
        t1 = abs(xi - t[left])
        t2 = abs(xi - t[left - 1]) if left > 0 else 10 ** 10
        ans = min(s1, s2, t1, t2)
        print(ans)
    return

=======
Suggestion 6

def search(a,b,query):
    a = list(map(int, a))
    b = list(map(int, b))
    query = list(map(int, query))
    result = []
    for q in query:
        a.append(q)
        b.append(q)
        a.sort()
        b.sort()
        aindex = a.index(q)
        bindex = b.index(q)
        if aindex == 0:
            amin = a[aindex]
        else:
            amin = q - a[aindex-1]
        if bindex == 0:
            bmin = b[bindex]
        else:
            bmin = q - b[bindex-1]
        result.append(min(amin,bmin))
    return result

=======
Suggestion 7

def main():
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    s.append(2 * 10 ** 10)
    t.append(2 * 10 ** 10)
    s = [-2 * 10 ** 10] + s
    t = [-2 * 10 ** 10] + t
    for i in range(Q):
        ans = 10 ** 20
        for j in range(A + 1):
            for k in range(B + 1):
                d = min(abs(x[i] - s[j]), abs(x[i] - t[k]))
                d += abs(s[j] - t[k])
                ans = min(ans, d)
        print(ans)

=======
Suggestion 8

def main():
    A, B, Q = map(int, input().split())
    s = [0] * (A + 2)
    t = [0] * (B + 2)
    x = [0] * (Q + 2)
    for i in range(1, A + 1):
        s[i] = int(input())
    for i in range(1, B + 1):
        t[i] = int(input())
    for i in range(1, Q + 1):
        x[i] = int(input())
    s[0] = -float('inf')
    s[A + 1] = float('inf')
    t[0] = -float('inf')
    t[B + 1] = float('inf')
    for i in range(1, Q + 1):
        j = 0
        while s[j] < x[i]:
            j += 1
        k = 0
        while t[k] < x[i]:
            k += 1
        print(min(max(x[i] - s[j - 1], t[k] - x[i]) + min(x[i] - s[j - 1], t[k] - x[i]), max(s[j] - x[i], x[i] - t[k - 1]) + min(s[j] - x[i], x[i] - t[k - 1])))

=======
Suggestion 9

def binarySearch(x, l):
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = (left + right) // 2
        if l[mid] == x:
            return mid
        elif l[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
x = [int(input()) for _ in range(Q)]

INF = 10**20
s = [-INF] + s + [INF]
t = [-INF] + t + [INF]

for i in range(Q):
    ans = INF
    a = binarySearch(x[i], s)
    b = binarySearch(x[i], t)
    for S in [s[a], s[a+1]]:
        for T in [t[b], t[b+1]]:
            d1 = abs(x[i] - S) + abs(S - T)
            d2 = abs(x[i] - T) + abs(T - S)
            ans = min(ans, d1, d2)
    print(ans)
