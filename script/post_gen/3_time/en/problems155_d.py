Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] >= 0:
        print(A[K-1])
    elif A[N-1] <= 0:
        if K % 2 == 0:
            print(abs(A[N-K]))
        else:
            print(A[N-K])
    else:
        if K % 2 == 0:
            if abs(A[0]) > A[N-1]:
                print(abs(A[N-K]))
            else:
                print(A[K-1])
        else:
            print(A[K-1])

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    l = -10**18
    r = 10**18
    while r - l > 1:
        m = (l + r) // 2
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                cnt += n - (n - i - 1) - 1
                for j in range(i + 1, n):
                    if a[i] * a[j] <= m:
                        cnt += 1
                    else:
                        break
            else:
                for j in range(i + 1, n):
                    if a[i] * a[j] <= m:
                        cnt += 1
                    else:
                        break
        if cnt < k:
            l = m
        else:
            r = m
    print(r)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ng = -10 ** 18
    ok = 10 ** 18
    while ok - ng > 1:
        mid = (ok + ng) // 2
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                l = 0
                r = n
                while r - l > 1:
                    c = (l + r) // 2
                    if a[i] * a[c] < mid:
                        l = c
                    else:
                        r = c
                cnt += n - r
            else:
                l = 0
                r = n
                while r - l > 1:
                    c = (l + r) // 2
                    if a[i] * a[c] < mid:
                        l = c
                    else:
                        r = c
                cnt += r
            if a[i] * a[i] < mid:
                cnt -= 1
        if cnt // 2 < k:
            ng = mid
        else:
            ok = mid
    print(ok)

main()

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    if A[0] >= 0:
        ans = A[K-1]
    else:
        if A[N-1] <= 0:
            if K % 2 == 0:
                ans = A[N-1]
            else:
                ans = A[0]
        else:
            if K % 2 == 0:
                if abs(A[0]) > A[N-1]:
                    ans = A[0]
                else:
                    ans = A[N-1]
            else:
                ans = A[K-1]
    print(ans)

main()

=======
Suggestion 5

def main():
    from sys import stdin
    from bisect import bisect_left
    _ = [int(x) for x in stdin.readline().split()]
    N = _[0]
    K = _[1]
    A = [int(x) for x in stdin.readline().split()]
    A.sort()
    #print(A)
    def count_less_than_or_equal_to(x):
        #print("x=",x)
        count = 0
        for i in range(N):
            if A[i] == 0:
                if x >= 0:
                    count += N
                break
            elif A[i] < 0:
                if x >= 0:
                    count += N - bisect_left(A, -(-x//A[i]))
                else:
                    count += bisect_left(A, -(-x//A[i]))
            else:
                if x >= 0:
                    count += bisect_left(A, x//A[i])
                else:
                    count += N - bisect_left(A, -(-x//A[i]))
        #print("count=",count)
        return count
    ok = -10**18
    ng = 10**18
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if count_less_than_or_equal_to(mid) >= K:
            ng = mid
        else:
            ok = mid
    print(ng)

=======
Suggestion 6

def main():
    import sys
    import bisect

    def input(): return sys.stdin.readline().rstrip()

    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A

    # A[i] * A[j] < A[k] * A[l] となる組み合わせの数を求める
    def count(a, b):
        if a == b:
            return N - a
        elif a < b:
            return bisect.bisect_left(A, (A[K] + A[a] - 1) // A[a]) - b
        else:
            return bisect.bisect_left(A, (A[K] + A[b] - 1) // A[b]) - a

    ans = 0
    for i in range(N):
        for j in range(i + 1, N + 1):
            ans += count(i, j)
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(K)
    if A[0] >= 0:
        print(A[K-1])
    elif A[N-1] <= 0:
        if K % 2 == 1:
            print(A[N-K])
        else:
            print(A[N-K+1])
    else:
        l = 0
        r = N-1
        while r-l > 1:
            m = (l+r)//2
            if A[m] < 0:
                l = m
            else:
                r = m
        #print(l)
        #print(r)
        if K <= (l+1)*(N-r):
            l = 0
            r = N-1
            while r-l > 1:
                m = (l+r)//2
                if A[m] < 0:
                    l = m
                else:
                    r = m
            #print(l)
            #print(r)
            if K <= (l+1)*(N-r):
                while True:
                    m = (l+r)//2
                    #print(l)
                    #print(r)
                    #print(m)
                    #print(A[l])
                    #print(A[r])
                    #print(A[m])
                    if A[m]*A[l] > A[m]*A[r]:
                        l = m
                    else:
                        r = m
                    if r-l == 1:
                        break
                #print(l)
                #print(r)
                #print(A[l])
                #print(A[r])
                print(A[l])
            else:
                K = K - (l+1)*(N-r)
                l = 0
                r = N-1
                while r-l > 1:
                    m = (l+r)//2
                    if A[m] < 0:
                        l = m
                    else:
                        r = m
                #print(l)
                #print(r)
                while True:
                    m = (l+r)//2
                    #print(l)
                    #print(r)
                    #print(m)
                    #print(A[l])
                    #print(A[r])
                    #print(A[m])
                    if A[m]*A[l] > A[m]*A[r]:
                        l = m

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()
    A = [0] + A + [0]

    # A[i] <= A[j] となる組み合わせの個数を求める
    def count(i, j):
        if A[i] * A[j] >= 0:
            return (j - i) * (j - i - 1) // 2
        else:
            left = 0
            right = j
            while right - left > 1:
                mid = (left + right) // 2
                if A[mid] * A[j] < 0:
                    left = mid
                else:
                    right = mid
            return (j - i) * (j - right) - (j - right) * (j - right - 1) // 2

    # 二分探索
    left = -10 ** 18
    right = 10 ** 18
    while right - left > 1:
        mid = (left + right) // 2
        cnt = 0
        for i in range(N + 1):
            if A[i] * A[i] > mid:
                continue
            left = 0
            right = N + 1
            while right - left > 1:
                j = (left + right) // 2
                if A[i] * A[j] <= mid:
                    left = j
                else:
                    right = j
            cnt += count(i, left)
        if cnt >= K:
            right = mid
        else:
            left = mid

    print(right)

=======
Suggestion 9

def isNegative(num):
    if num < 0:
        return True
    else:
        return False

=======
Suggestion 10

def get_input():
    f = open('input.txt')
    return f
