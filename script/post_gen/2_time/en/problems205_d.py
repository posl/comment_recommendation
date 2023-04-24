Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    ans = []
    for k in K:
        l, r = 1, 10**18
        while r - l > 1:
            m = (l + r) // 2
            if sum(m // a for a in A) < k:
                l = m
            else:
                r = m
        ans.append(r)
    print('

'.join(map(str, ans)))

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    #print(N, Q, A, K)

    # 1. 1, 2, 4, 8, 9, 10, 11, ... のように、Aの間隔の倍数の数列を作る
    # 2. 1.の数列にAを足す
    # 3. 2.の数列にKを足す
    # 4. 3.の数列に1を足す
    # 5. 4.の数列をソートする
    # 6. 5.の数列のK番目の要素を出力する
    B = [1]
    for i in range(N-1):
        B.append(B[i] + A[i+1] - A[i])
    #print(B)
    C = []
    for b in B:
        for k in K:
            C.append(b + k)
    #print(C)
    D = sorted(C)
    #print(D)
    for i in range(Q):
        print(D[i])

=======
Suggestion 3

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A = [0] + A + [10**18]
    D = []
    for i in range(N+1):
        D.append(A[i+1] - A[i] - 1)
    D.sort(reverse=True)
    for k in K:
        if k <= D[0]:
            print(k)
        else:
            k -= D[0]
            print(A[N] + (k + N - 1) // N)

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]

    for i in range(q):
        l, r = 0, 10**18
        while r - l > 1:
            mid = (l + r) // 2
            if sum(mid // ai for ai in a) >= k[i]:
                r = mid
            else:
                l = mid
        print(r)

=======
Suggestion 5

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    ans = []
    for k in K:
        l, r = 0, 10**18
        while r - l > 1:
            m = (l + r) // 2
            cnt = 0
            for a in A:
                cnt += (m + a - 1) // a
            if cnt >= k:
                r = m
            else:
                l = m
        ans.append(r)
    print('

'.join(map(str, ans)))

solve()

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    a.append(0)
    a.append(10**18 + 1)
    a.sort()
    for i in range(q):
        l, r = 0, n + 1
        while r - l > 1:
            m = (l + r) // 2
            if a[m] - a[m - 1] - 1 < k[i]:
                k[i] -= a[m] - a[m - 1] - 1
                l = m
            else:
                r = m
        print(k[i] + a[l])

=======
Suggestion 7

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    INF = 10**18
    A.append(INF)
    A.append(-INF)
    A.sort()
    for k in K:
        l = 0
        r = N+1
        while r-l > 1:
            m = (l+r)//2
            if A[m] - A[m-1] < k:
                k -= A[m] - A[m-1]
                l = m
            else:
                r = m
        print(A[l] + k)

=======
Suggestion 8

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]

    def f(num):
        for i in range(n):
            if num <= a[i]:
                return num
            num += 1
        return num

    for i in range(q):
        print(f(k[i]))

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]

    # 1. Aの隣り合う要素の差を求める
    # 2. 差の中にK[i]を入れることができるかを二分探索で探す
    # 3. 2.で見つけた差の中で最小のものをK[i]に加える
    # 4. 3.で求めた値をAに挿入する
    # 5. 1.に戻る
    for i in range(Q):
        diff = []
        for j in range(N - 1):
            diff.append(A[j + 1] - A[j])
        ok = -1
        ng = N
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if diff[mid] > K[i]:
                ng = mid
            else:
                ok = mid
        if ok == -1:
            ans = A[0] + K[i]
        elif ok == N - 1:
            ans = A[N - 1] + K[i] - diff[ok - 1]
        else:
            ans = A[ok] + K[i] - diff[ok - 1]
        A.append(ans)
        A.sort()
        print(ans)

=======
Suggestion 10

def solve():
    # read input
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]

    # 答えを格納する配列
    ans = [0] * Q

    # クエリについて二分探索
    for i in range(Q):
        # 二分探索の左端と右端
        left = 1
        right = 10 ** 18 + 1

        # 二分探索
        while right - left > 1:
            mid = (left + right) // 2

            # mid が A の各要素との差の中央値以上であるかを判定
            if is_ok(mid, A):
                left = mid
            else:
                right = mid

        # クエリの答えを格納
        ans[i] = left

    # 答えを出力
    for i in range(Q):
        print(ans[i])
