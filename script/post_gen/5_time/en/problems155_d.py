Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    l = -10**18
    r = 10**18
    while r - l > 1:
        mid = (r + l) // 2
        cnt = 0
        for i in range(N):
            if A[i] < 0:
                cnt += N - bisect_left(A, (-mid - 1) // A[i])
            elif A[i] > 0:
                cnt += bisect_left(A, (mid - 1) // A[i])
            else:
                if mid > 0:
                    cnt += N
        cnt //= 2
        if cnt < K:
            l = mid
        else:
            r = mid
    print(r)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    INF = 10 ** 18
    left = -INF
    right = INF
    while left + 1 < right:
        mid = (left + right) // 2
        count = 0
        for i in range(N):
            if A[i] < 0:
                l = -1
                r = N
                while l + 1 < r:
                    m = (l + r) // 2
                    if A[m] * A[i] < mid:
                        r = m
                    else:
                        l = m
                count += N - r
            else:
                l = -1
                r = N
                while l + 1 < r:
                    m = (l + r) // 2
                    if A[m] * A[i] < mid:
                        l = m
                    else:
                        r = m
                count += r
            if A[i] * A[i] < mid:
                count -= 1
        count //= 2
        if count < K:
            left = mid
        else:
            right = mid
    print(right)

=======
Suggestion 4

def solve(N, K, A):
    A.sort()
    l = -10**18
    r = 10**18
    while l + 1 < r:
        m = (l + r) // 2
        cnt = 0
        for i in range(N):
            if A[i] < 0:
                cnt += N - bisect.bisect_left(A, m // A[i])
            elif A[i] > 0:
                cnt += bisect.bisect_right(A, m // A[i])
            else:
                if m >= 0:
                    cnt += N
        cnt //= 2
        if cnt >= K:
            r = m
        else:
            l = m
    return r

=======
Suggestion 5

def solve(N, K, A):
    A.sort()
    l = -10**18
    r = 10**18
    while r - l > 1:
        m = (l + r) // 2
        cnt = 0
        for i in range(N):
            if A[i] > 0:
                cnt += bisect.bisect_right(A, m // A[i])
            elif A[i] < 0:
                cnt += N - bisect.bisect_right(A, m // A[i])
            else:
                if m >= 0:
                    cnt += N
                else:
                    cnt += N - i - 1
        cnt //= 2
        if cnt < K:
            l = m
        else:
            r = m
    return l

import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))
print(solve(N, K, A))

=======
Suggestion 6

def solve(n, k, a):
    a.sort()
    l = -10**18
    r = 10**18
    while l + 1 < r:
        x = (l + r) // 2
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                cnt += n - bisect.bisect_left(a, x // a[i])
            elif a[i] == 0:
                if x >= 0:
                    cnt += n
            else:
                cnt += bisect.bisect_right(a, x // a[i])
            if a[i] * a[i] <= x:
                cnt -= 1
        cnt //= 2
        if cnt >= k:
            r = x
        else:
            l = x
    return r

import bisect
n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    min_value = -10**18 - 1
    max_value = 10**18 + 1
    while max_value - min_value > 1:
        mid = (max_value + min_value) // 2
        count = 0
        j = N - 1
        for i in range(N):
            while j >= 0 and A[i] * A[j] <= mid:
                j -= 1
            count += N - 1 - j
        if count >= K:
            max_value = mid
        else:
            min_value = mid
    print(max_value)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    mod = 10**9 + 7
    pos = 0
    neg = 0
    for i in range(n):
        if a[i] < 0:
            neg += 1
        else:
            pos += 1
    if neg * pos >= k:
        l = -10**18
        r = 10**18
        while r - l > 1:
            x = (l + r) // 2
            cnt = 0
            for i in range(n):
                if a[i] < 0:
                    cnt += n - bisect.bisect_right(a, x // a[i])
                else:
                    cnt += bisect.bisect_left(a, x // a[i])
                if a[i] * a[i] <= x:
                    cnt -= 1
            cnt //= 2
            if cnt >= k:
                r = x
            else:
                l = x
        print(r)
    else:
        l = -10**18
        r = 10**18
        while r - l > 1:
            x = (l + r) // 2
            cnt = 0
            for i in range(n):
                if a[i] < 0:
                    cnt += bisect.bisect_left(a, x // a[i])
                else:
                    cnt += n - bisect.bisect_right(a, x // a[i])
                if a[i] * a[i] <= x:
                    cnt -= 1
            cnt //= 2
            if cnt >= k:
                r = x
            else:
                l = x
        print(r)

=======
Suggestion 9

def solve():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    a.sort()

    def check(x):
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                l = -1
                r = n
                while r - l > 1:
                    m = (l + r) // 2
                    if a[m] * a[i] < x:
                        r = m
                    else:
                        l = m
                cnt += n - r
            elif a[i] == 0:
                if x > 0:
                    cnt += n
            else:
                l = -1
                r = n
                while r - l > 1:
                    m = (l + r) // 2
                    if a[m] * a[i] < x:
                        l = m
                    else:
                        r = m
                cnt += r
                if a[i] * a[i] < x:
                    cnt -= 1
        cnt //= 2
        return cnt < k

    l = -10 ** 18
    r = 10 ** 18
    while r - l > 1:
        m = (l + r) // 2
        if check(m):
            l = m
        else:
            r = m
    print(r)


solve()

=======
Suggestion 10

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    import bisect
    def check(x):
        # x以下のペアの数がK個以上あるかどうか
        # 合計O(N log N)
        # 二分探索を使っている
        cnt = 0
        for i in range(N):
            if A[i] >= 0:
                break
            # A[i]を固定して、A[j]を二分探索で探す
            # 二分探索を使うことで、O(log N)
            # これをN回繰り返すので、合計O(N log N)
            cnt += bisect.bisect_left(A, (x + A[i] - 1) // A[i]) - i - 1
        if cnt >= K:
            return True
        else:
            return False

    # 二分探索
    # 最小値は負の数、最大値は正の数
    # 二分探索の終了条件は、最大値と最小値が隣り合った時
    l = -10 ** 18 - 1
    r = 10 ** 18 + 1
    while r - l > 1:
        m = (l + r) // 2
        if check(m):
            r = m
        else:
            l = m
    print(r)
