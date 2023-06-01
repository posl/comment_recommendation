Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    a.sort()
    max_a = a[-1]
    max_k = k[-1]
    b = [0] * (max_a+1)
    for i in range(n):
        b[a[i]] = 1
    c = [0] * (max_a+1)
    for i in range(1, max_a+1):
        c[i] = c[i-1] + b[i]
    for i in range(q):
        if k[i] > max_k:
            print(a[-1] + k[i] - max_k)
        else:
            print(c.index(k[i]))

=======
Suggestion 2

def binary_search(n, a, key):
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if key == a[mid]:
            return mid
        elif key > a[mid]:
            left = mid + 1
        else:
            right = mid
    return -1

=======
Suggestion 3

def get_next_num(num):
    if num == 0:
        return 1
    elif num == 1:
        return 2
    elif num == 2:
        return 4
    else:
        return num*2

=======
Suggestion 4

def find_kth_min(a, k):
    if k > a[-1]:
        return a[-1] + k - a[-1]
    if k < a[0]:
        return k
    l = 0
    r = len(a) - 1
    while l < r:
        m = (l + r) // 2
        if a[m] < k:
            l = m + 1
        else:
            r = m
    return a[l] + k - a[l]

=======
Suggestion 5

def get_ints():
    return map(int, raw_input().split())

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    a.sort()
    i = 0
    j = 0
    while i < q:
        if j < n:
            if k[i] == a[j]:
                j += 1
            else:
                k[i] -= j
                i += 1
        else:
            k[i] -= j
            i += 1
    for i in k:
        print(i)

=======
Suggestion 7

def find_kth_number(k, nums):
    if k == 1:
        return 1

    num = 1
    while k > 1:
        num += 1
        if num not in nums:
            k -= 1
    return num

=======
Suggestion 8

def get_min_num_not_in_a_list(a):
    if not a:
        return 1
    if a[-1] == len(a):
        return len(a) + 1
    for i in range(1, len(a)):
        if a[i] - a[i-1] > 1:
            return a[i-1] + 1

=======
Suggestion 9

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    a.sort()
    a.append(float('inf'))
    j = 0
    for i in range(q):
        while k[i] > a[j]:
            k[i] += 1
            j += 1
        print(k[i])

=======
Suggestion 10

def main():
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    k = []
    for i in range(q):
        k.append(int(input()))

    a.sort()
    ans = []
    for i in range(q):
        tmp = k[i]
        for j in range(n):
            if tmp < a[j]:
                ans.append(tmp)
                break
            else:
                tmp += 1
                continue
        else:
            ans.append(tmp)

    for i in range(q):
        print(ans[i])
