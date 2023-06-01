Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(A)
    #print(A[K-1])
    #print(A[0])
    #print(A[N-1])
    #print(A[N-1]*A[N-2])
    #print(A[0]*A[1])
    #print(A[0]*A[N-1])
    #print(A[0]*A[1])
    #print(A

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = a[::-1]
    print(a)
    l = -10**18
    r = 10**18
    while r - l > 1:
        mid = (r + l) // 2
        cnt = 0
        for i in range(n):
            if a[i] > 0:
                cnt += n - i - 1
                continue
            if a[i] == 0:
                continue
            ok = n
            ng = i
            while ok - ng > 1:
                m = (ok + ng) // 2
                if a[i] * a[m] > mid:
                    ok = m
                else:
                    ng = m
            cnt += n - ok
        if cnt >= k:
            r = mid
        else:
            l = mid
    print(r)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    left = -10**18
    right = 10**18
    while right - left > 1:
        mid = (left + right) // 2
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                l = -1
                r = n
                while r - l > 1:
                    m = (l + r) // 2
                    if a[i] * a[m] < mid:
                        r = m
                    else:
                        l = m
                cnt += n - r
            else:
                l = -1
                r = n
                while r - l > 1:
                    m = (l + r) // 2
                    if a[i] * a[m] < mid:
                        l = m
                    else:
                        r = m
                cnt += r
            if a[i] * a[i] < mid:
                cnt -= 1
        cnt //= 2
        if cnt < k:
            left = mid
        else:
            right = mid
    print(left)

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    left = -10**18
    right = 10**18
    while left + 1 < right:
        mid = (left + right) // 2
        #print(left, mid, right)
        cnt = 0
        for i in range(N):
            if A[i] < 0:
                l = -1
                r = N
                while l + 1 < r:
                    m = (l + r) // 2
                    if A[i] * A[m] <= mid:
                        r = m
                    else:
                        l = m
                cnt += N - r
            else:
                l = -1
                r = N
                while l + 1 < r:
                    m = (l + r) // 2
                    if A[i] * A[m] <= mid:
                        l = m
                    else:
                        r = m
                cnt += r
            if A[i] * A[i] <= mid:
                cnt -= 1
        cnt = cnt // 2
        #print(cnt)
        if cnt < K:
            left = mid
        else:
            right = mid
    print(right)

solve()

=======
Suggestion 5

def solve():
    # 入力
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 0の数
    num_zero = a.count(0)
    # 0の数だけ0の組み合わせがある
    if num_zero > 0:
        k -= num_zero * (n - num_zero)
        # 0がk番目に来る場合
        if k <= 0:
            print(0)
            return
    # 0を除いた数値に変換
    a = [x for x in a if x != 0]
    # 昇順に並べる
    a.sort(key=abs)
    # 負の数の数
    num_minus = len([x for x in a if x < 0])
    # 負の数の数が奇数の場合
    if num_minus % 2 == 1:
        # 0がk番目に来る場合
        if k <= 0:
            print(0)
            return
        # 負の数をk番目に来るように調整
        a = a[1:]
        k -= 1
    # 0を除いた数値の数
    n = len(a)
    # 0を除いた数値の数の組み合わせの数
    num_comb = n * (n - 1) // 2
    # kが大きすぎる場合
    if k > num_comb:
        print(0)
        return
    # k番目の数値を出力
    print(a[k - 1])

solve()

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    #print(A)
    #print(A[0]*A[1])
    #print(A[-1]*A[-2])
    #print(A[0]*A[-1])
    #print(A[1]*A[-1])
    #print(A[0]*A[-2])
    if A[0] >= 0:
        print(A[K-1]*A[K-2])
    elif A[-1] < 0:
        if K%2 == 0:
            print(A[K-1]*A[K-2])
        else:
            print(A[K-1]*A[K-2])
    else:
        if K%2 == 0:
            print(A[K-1]*A[K-2])
        else:
            if A[0]*A[1] < A[-1]*A[-2]:
                print(A[K-1]*A[K-2])
            else:
                print(A[0]*A[1])

=======
Suggestion 7

def f(n, k, a):
    a.sort()
    a = [x for x in a if x < 0]
    b = [x for x in a if x >= 0]
    a.reverse()
    if k <= len(a) * len(b):
        return 0
    else:
        k -= len(a) * len(b)
    while len(a) > 0 and len(b) > 0:
        if k == 1:
            return a[0] * b[0]
        elif k == 2:
            if len(a) > 1 and len(b) > 1:
                return max(a[0] * a[1], b[0] * b[1])
            elif len(a) > 1:
                return a[0] * a[1]
            else:
                return b[0] * b[1]
        elif k == 3:
            if len(a) > 1 and len(b) > 1:
                return max(a[0] * a[1] * a[2], b[0] * b[1] * b[2])
            elif len(a) > 1:
                return a[0] * a[1]
            else:
                return b[0] * b[1]
        else:
            if len(a) > 1 and len(b) > 1:
                return max(a[0] * a[1], b[0] * b[1])
            elif len(a) > 1:
                return a[0] * a[1]
            else:
                return b[0] * b[1]
    return 0

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    left = -10**18
    right = 10**18
    while left + 1 < right:
        mid = (left + right) // 2
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                l = -1
                r = n
                while l + 1 < r:
                    m = (l + r) // 2
                    if a[m] * a[i] < mid:
                        r = m
                    else:
                        l = m
                cnt += n - r
            else:
                l = -1
                r = n
                while l + 1 < r:
                    m = (l + r) // 2
                    if a[m] * a[i] < mid:
                        l = m
                    else:
                        r = m
                cnt += r
            if a[i] * a[i] < mid:
                cnt -= 1
        cnt //= 2
        if cnt < k:
            left = mid
        else:
            right = mid
    print(left)

=======
Suggestion 9

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [a for a in A if a < 0] + [0] + [a for a in A if a > 0]
    l = len(A)
    def f(x):
        c = 0
        for a in A:
            if a < 0:
                c += l
            elif a == 0:
                c += l - 1
            else:
                break
            if c >= K:
                return True
        for i in range(l):
            for j in range(i + 1, l):
                if A[i] * A[j] <= x:
                    c += 1
                else:
                    break
                if c >= K:
                    return True
        return False
    ok = 10**18 + 1
    ng = -10**18 - 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(solve())

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()

    #print(n,k)
    #print(a)
    #print(a[n-1],a[n-2],a[n-3],a[n-4],a[n-5],a[n-6])

    if n==2:
        print(a[0]*a[1])
        return

    if a[n-1]>=0:
        if k<=((n*(n-1))/2):
            print(a[n-1]*a[n-2-(k-1)])
        else:
            print(a[0]*a[n-1])
    elif a[n-1]<0:
        if k<=((n*(n-1))/2):
            print(a[0]*a[1+(k-1)])
        else:
            print(a[0]*a[n-1])
