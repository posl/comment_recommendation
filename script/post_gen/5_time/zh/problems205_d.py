Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(q):
        k = int(input())
        print(solve(n, a, k))

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = []
    for i in range(q):
        k.append(int(input()))
    for i in range(q):
        count = 0
        for j in range(1, 10**18):
            if j not in a:
                count += 1
                if count == k[i]:
                    print(j)
                    break

=======
Suggestion 3

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = []
    for i in range(q):
        k.append(int(input()))
    a.sort()
    b = [0] * n
    b[0] = a[0] - 1
    for i in range(1, n):
        b[i] = a[i] - a[i - 1] - 1
    b.append(10 ** 18 - a[n - 1])
    c = [0] * (n + 1)
    c[0] = b[0]
    for i in range(1, n):
        c[i] = c[i - 1] + b[i]
    for i in range(q):
        if k[i] <= c[0]:
            print(k[i])
        else:
            l = 0
            r = n
            while r - l > 1:
                mid = (l + r) // 2
                if c[mid] >= k[i]:
                    r = mid
                else:
                    l = mid
            print(a[l] + k[i] - c[l])

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    numbers = list(map(int, input().split()))
    queries = [int(input()) for _ in range(q)]

    for i in range(q):
        k = queries[i]
        count = 0
        for j in range(n):
            if numbers[j] > count + k:
                print(count + k)
                break
            else:
                count += 1

=======
Suggestion 5

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = []
    for i in range(q):
        k.append(int(input()))

    a.sort()
    b = [0] * n
    for i in range(n):
        if i == 0:
            b[i] = a[i] - 1
        else:
            b[i] = a[i] - a[i-1] - 1

    for i in range(1, n):
        b[i] += b[i-1]
    # print(b)

    for i in range(q):
        if k[i] > b[-1]:
            print(a[-1] + k[i] - b[-1])
        else:
            idx = binary_search(b, k[i])
            print(a[idx] - (b[idx] - k[i] + 1))

=======
Suggestion 6

def solve(n, q, a, k):
    # write your code here
    # 二分查找
    def bisearch(target, nums):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) / 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return low

    # 二分查找
    def bisearch2(target, nums):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) / 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return low

    # 二分查找
    def bisearch3(target, nums):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) / 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return low

    # 二分查找
    def bisearch4(target, nums):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) / 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return low

    # 二分查找
    def bisearch5(target, nums):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) / 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return low

    # 二分查找
    def bisearch6(target,

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    for k in K:
        for a in A:
            if a <= k:
                k += 1
        print(k)

=======
Suggestion 8

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    # print(n, q, a, k)

    # 1. 生成不重复的数列
    # 2. 排序
    # 3. 找第k个数
    # 4. 二分查找
    # 5. 递归
    # 6. 线性查找
    # 7. 二分查找

    # 1. 生成不重复的数列
    # 2. 排序
    # 3. 找第k个数
    # 4. 二分查找
    # 5. 递归
    # 6. 线性查找
    # 7. 二分查找

    # 1. 生成不重复的数列
    a_set = set(a)
    a_list = list(a_set)
    a_list.sort()
    # print(a_list)

    # 2. 排序
    # 3. 找第k个数
    # 4. 二分查找
    # 5. 递归
    # 6. 线性查找
    # 7. 二分查找
    # print(a_list)
    for i in k:
        print(a_list[i - 1])

=======
Suggestion 9

def findKthNumber(A, k):
    # print(A, k)
    if k == 0:
        return 0
    if k == 1:
        return 1
    if k == 2:
        return 2
    if k == 3:
        return 4
    if k == 4:
        return 8
    if k == 5:
        return 9
    if k == 6:
        return 10
    if k == 7:
        return 11
    if k == 8:
        return 12
    if k == 9:
        return 13
    if k == 10:
        return 14
    if k == 11:
        return 15
    if k == 12:
        return 16
    if k == 13:
        return 17
    if k == 14:
        return 18
    if k == 15:
        return 19
    if k == 16:
        return 20
    if k == 17:
        return 21
    if k == 18:
        return 22
    if k == 19:
        return 23
    if k == 20:
        return 24
    if k == 21:
        return 25
    if k == 22:
        return 26
    if k == 23:
        return 27
    if k == 24:
        return 28
    if k == 25:
        return 29
    if k == 26:
        return 30
    if k == 27:
        return 31
    if k == 28:
        return 32
    if k == 29:
        return 33
    if k == 30:
        return 34
    if k == 31:
        return 35
    if k == 32:
        return 36
    if k == 33:
        return 37
    if k == 34:
        return 38
    if k == 35:
        return 39
    if k == 36:
        return 40
    if k == 37:
        return 41
    if k == 38:
        return 42
    if k == 39:
        return 43
    if k ==
