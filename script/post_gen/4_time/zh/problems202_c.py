Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))
    d = [0] * n
    for i in range(n):
        d[b[c[i]]] += 1
    print(sum([d[a[i]] for i in range(n)]))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    #print(N)
    #print(A)
    #print(B)
    #print(C)

    count = 0
    A.sort()
    B.sort()
    C.sort()
    #print(A)
    #print(B)
    #print(C)
    i = 0
    j = 0
    k = 0
    while i < N and j < N and k < N:
        if A[i] == B[C[j] - 1]:
            count += 1
            i += 1
            j += 1
        elif A[i] < B[C[j] - 1]:
            i += 1
        else:
            j += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))
    d = [0] * n
    for i in range(n):
        d[b[c[i]]] += 1
    ans = 0
    for i in range(n):
        ans += d[a[i]]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x)-1, input().split()))
    d = {}
    for i in range(n):
        if b[c[i]] in d:
            d[b[c[i]]] += 1
        else:
            d[b[c[i]]] = 1
    ans = 0
    for i in range(n):
        if a[i] in d:
            ans += d[a[i]]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = [0] * (n + 1)
    for j in c:
        d[b[j - 1]] += 1
    ans = 0
    for i in a:
        ans += d[i]
    print(ans)

=======
Suggestion 6

def count_pairs(n, a, b, c):
    count = 0
    for i in range(n):
        for j in range(n):
            if a[i] == b[c[j] - 1]:
                count += 1
    return count

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B_C = []
    for i in range(N):
        B_C.append(B[C[i]-1])

    B_C.sort()
    A.sort()

    count = 0
    for i in range(N):
        if A[i] == B_C[i]:
            count += 1

    print(count)

=======
Suggestion 8

def get_n():
    n = int(input())
    return n

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    c = list(map(int, input().split(' ')))

    a_dict = {}
    b_dict = {}
    c_dict = {}
    for i in range(n):
        a_dict[a[i]] = a_dict.get(a[i], 0) + 1
        b_dict[b[i]] = b_dict.get(b[i], 0) + 1
        c_dict[c[i]] = c_dict.get(c[i], 0) + 1

    result = 0
    for i in range(1, n + 1):
        if i in c_dict:
            result += a_dict.get(b_dict.get(c_dict[i], 0), 0)

    print(result)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    # 1. 暴力
    # ans = 0
    # for i in range(n):
    #     for j in range(n):
    #         if a[i] == b[c[j]-1]:
    #             ans += 1
    # print(ans)

    # 2. 哈希表
    # ans = 0
    # c_dict = {}
    # for i in range(n):
    #     if c[i] not in c_dict:
    #         c_dict[c[i]] = 1
    #     else:
    #         c_dict[c[i]] += 1
    #
    # for i in range(n):
    #     if a[i] in c_dict:
    #         ans += c_dict[a[i]]
    #
    # print(ans)

    # 3. 二分查找
    # ans = 0
    # c.sort()
    # for i in range(n):
    #     if a[i] in c:
    #         # 二分查找
    #         left = 0
    #         right = n - 1
    #         while left <= right:
    #             mid = (left + right) // 2
    #             if c[mid] == a[i]:
    #                 ans += 1
    #                 break
    #             elif c[mid] < a[i]:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    # print(ans)

    # 4. 二分查找
    ans = 0
    c.sort()
    for i in range(n):
        if a[i] in c:
            # 二分查找
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if c[mid] == a[i]:
                    ans += 1
                    # 从c中删除匹配的元素，防止重复计数
                    del c[mid]
                    break
                elif c[mid] < a[i]:
