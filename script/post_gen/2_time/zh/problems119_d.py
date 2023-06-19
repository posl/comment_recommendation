Synthesizing 10/10 solutions

=======
Suggestion 1

def search(s,t,x):
    i = 0
    j = 0
    while i < len(s) and s[i] < x:
        i += 1
    while j < len(t) and t[j] < x:
        j += 1
    if i == 0:
        return t[j] - x
    elif j == 0:
        return s[i] - x
    else:
        return min(s[i] - x + s[i] - t[j-1], t[j] - x + t[j] - s[i-1], s[i] - x + t[j] - x, s[i] - x + t[j] - x)

=======
Suggestion 2

def main():
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    s.append(10**11)
    t.append(10**11)
    from bisect import bisect_left, bisect_right
    for i in range(Q):
        j = bisect_left(s, x[i])
        k = bisect_left(t, x[i])
        ans = 10**11
        for sj in [s[j-1], s[j]]:
            for tk in [t[k-1], t[k]]:
                ans = min(ans, abs(sj-x[i])+abs(tk-sj), abs(tk-x[i])+abs(sj-tk))
        print(ans)

main()

=======
Suggestion 3

def find_nearest(arr, x):
    n = len(arr)
    if x <= arr[0]:
        return arr[0]
    if x >= arr[n-1]:
        return arr[n-1]
    i = 0
    j = n
    mid = 0
    while i < j:
        mid = (i+j)//2
        if arr[mid] == x:
            return arr[mid]
        if x < arr[mid]:
            if mid > 0 and x > arr[mid-1]:
                return get_closest(arr[mid-1], arr[mid], x)
            j = mid
        else:
            if mid < n-1 and x < arr[mid+1]:
                return get_closest(arr[mid], arr[mid+1], x)
            i = mid + 1
    return arr[mid]

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def binary_search(a,x):
    left = 0
    right = len(a)-1
    while left <= right:
        mid = int((left + right)/2)
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left

a,b,q = map(int,input().split())
s = []
t = []
for i in range(a):
    s.append(int(input()))
for i in range(b):
    t.append(int(input()))
for i in range(q):
    x = int(input())
    x1 = binary_search(s,x)
    x2 = binary_search(t,x)
    ans = 10**20
    for ss in s[x1-1:x1+1]:
        for tt in t[x2-1:x2+1]:
            d1 = abs(ss-x) + abs(tt-ss)
            d2 = abs(tt-x) + abs(ss-tt)
            ans = min(ans,d1,d2)
    print(ans)

=======
Suggestion 6

def binary_search(array, value):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == value:
            return middle
        elif array[middle] < value:
            left = middle + 1
        else:
            right = middle - 1
    return left

=======
Suggestion 7

def get_input():
    input = []
    while True:
        try:
            input.append(raw_input())
        except EOFError:
            break
    return input

=======
Suggestion 8

def main():
    a, b, q = map(int, input().split())
    s = [int(input()) for _ in range(a)]
    t = [int(input()) for _ in range(b)]
    x = [int(input()) for _ in range(q)]
    # print(s,t,x)
    for i in range(q):
        tmp = x[i]
        tmp_s = 0
        tmp_t = 0
        for j in range(a):
            if tmp >= s[j]:
                tmp_s = tmp - s[j]
            else:
                tmp_s = s[j] - tmp
            if j == 0:
                min_s = tmp_s
            else:
                if tmp_s < min_s:
                    min_s = tmp_s
        for j in range(b):
            if tmp >= t[j]:
                tmp_t = tmp - t[j]
            else:
                tmp_t = t[j] - tmp
            if j == 0:
                min_t = tmp_t
            else:
                if tmp_t < min_t:
                    min_t = tmp_t
        if min_s < min_t:
            print(min_t)
        else:
            print(min_s)

=======
Suggestion 9

def binary_search(target, array):
    """
    二分法查找
    :param target: 目标值
    :param array: 有序数组
    :return: 目标值在数组中的索引
    """
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if target > array[mid]:
            start = mid + 1
        elif target < array[mid]:
            end = mid - 1
        else:
            return mid
    return -1

=======
Suggestion 10

def main():
    a, b, q = map(int, input().split())
    s = [int(input()) for _ in range(a)]
    t = [int(input()) for _ in range(b)]
    x = [int(input()) for _ in range(q)]

    import bisect
    for i in range(q):
        ans = 10**20
        for shrine in [s[bisect.bisect_left(s, x[i]) - 1], s[bisect.bisect_right(s, x[i]) - 1]]:
            for temple in [t[bisect.bisect_left(t, x[i]) - 1], t[bisect.bisect_right(t, x[i]) - 1]]:
                d = abs(shrine - x[i]) + abs(shrine - temple)
                ans = min(ans, d)
                d = abs(temple - x[i]) + abs(temple - shrine)
                ans = min(ans, d)
        print(ans)
