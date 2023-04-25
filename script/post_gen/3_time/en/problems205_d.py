Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A = [0] + A + [10**18]
    for k in K:
        l, r = -1, N
        while l + 1 < r:
            m = (l + r) // 2
            if A[m] < A[m + 1] - A[m] + 1:
                k -= A[m + 1] - A[m] + 1
                l = m
            else:
                r = m
        print(A[l] + k)

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A = [0] + A + [10**18]
    for k in K:
        l, r = 0, N + 1
        while r - l > 1:
            m = (l + r) // 2
            if A[m] - A[m - 1] - 1 < k:
                k -= A[m] - A[m - 1] - 1
                l = m
            else:
                r = m
        print(A[l] + k)

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = A[i] - A[i - 1] - 1
    for i in range(N):
        B[i + 1] += B[i]
    for k in K:
        if k > B[N]:
            print(A[-1] + k - B[N])
            continue
        ok = 0
        ng = N
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if B[mid] >= k:
                ng = mid
            else:
                ok = mid
        print(A[ok] + k - B[ok])

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A = [0] + A
    A.append(10**18)
    for k in K:
        l = 0
        r = N + 1
        while r - l > 1:
            m = (r + l) // 2
            if A[m] - (m + 1) < k:
                l = m
            else:
                r = m
        print(l + k)

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]

    # Aの各要素との差を列挙
    diff = []
    for i in range(N-1):
        diff.append(A[i+1] - A[i] - 1)

    # 差の累積和を計算
    diff_sum = [0]
    for i in range(N-1):
        diff_sum.append(diff_sum[i] + diff[i])

    # 二分探索
    for k in K:
        # 二分探索の範囲を決める
        left = 0
        right = N-1
        while left <= right:
            mid = (left + right) // 2
            if diff_sum[mid] >= k:
                right = mid - 1
            else:
                left = mid + 1

        # 差の累積和がkを超えたところの左隣のインデックスが求まる
        # そのインデックスの左隣の要素との差を求める
        if left == 0:
            print(k)
        else:
            print(A[left-1] + k - diff_sum[left-1])

=======
Suggestion 6

def solve():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    K = [int(input()) for _ in range(Q)]
    for k in K:
        ok = 10**18
        ng = 0
        while ok-ng>1:
            mid = (ok+ng)//2
            if check(mid,A,k):
                ok = mid
            else:
                ng = mid
        print(ok)

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    
    def solve(K):
        if K <= A[0]-1:
            return K
        elif K >= A[-1]+1:
            return K + A[-1]
        
        ng = 0
        ok = N-1
        while ok-ng > 1:
            mid = (ok+ng)//2
            if A[mid] <= K:
                ng = mid
            else:
                ok = mid
        return K + A[ng]
    
    for k in K:
        print(solve(k))

=======
Suggestion 8

def main():
    #input
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]

    #compute
    #B[i] := A[i] - A[i-1] - 1
    B = [A[0]-1] + [A[i]-A[i-1]-1 for i in range(1, N)]
    #C[i] := B[0] + B[1] + ... + B[i]
    C = [B[0]] + [C[i-1]+B[i] for i in range(1, N)]
    #D[i] := D[i-1] + C[i-1] + 1
    D = [0] + [D[i-1]+C[i-1]+1 for i in range(1, N)]

    #output
    for k in K:
        #binary search
        #A[i] - D[i] <= k <= A[i+1] - D[i+1]
        left, right = 0, N
        while right - left > 1:
            mid = (left + right) // 2
            if A[mid] - D[mid] <= k:
                left = mid
            else:
                right = mid
        print(k + D[left])

=======
Suggestion 9

def main():
    #Read input
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    
    #Find the maximum value of Ai + 1
    max_value = 0
    for i in range(N - 1):
        max_value = max(max_value, A[i + 1] - A[i])
    
    #Find the minimum value of Ai + 1
    min_value = 10 ** 18
    for i in range(N - 1):
        min_value = min(min_value, A[i + 1] - A[i])
    
    #Find the minimum value of Ai + 1 that is greater than or equal to k
    for k in K:
        if k >= max_value:
            print(A[N - 1] + k - max_value)
        else:
            #Binary search
            left = 0
            right = N - 1
            while left < right:
                mid = (left + right) // 2
                if A[mid] + k >= A[mid + 1]:
                    left = mid + 1
                else:
                    right = mid
            print(A[left] + k)

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    # A[i] - A[i-1] - 1を計算する
    # 例えばA = [1, 2, 3, 4, 5]の場合、
    # A[i] - A[i-1] - 1 = [1, 1, 1, 1]
    # となる
    # これを累積和をとっておく
    # 例えばA = [1, 2, 3, 4, 5]の場合、
    # [1, 1, 1, 1]の累積和は[1, 2, 3, 4]となる
    # これがBとなる
    B = [0]
    for i in range(1, N):
        B.append(B[i-1] + A[i] - A[i-1] - 1)

    # これからクエリを処理していく
    for _ in range(Q):
        K = int(input())
        # KがBの最後の要素より大きい場合
        # 例えばA = [1, 2, 3, 4, 5]の場合、
        # B = [1, 2, 3, 4]となる
        # これはAの最後の要素からAの最初の要素までの距離が5-1-1=3であることを意味する
        # この場合、KがBの最後の要素より大きいということは
        # KはAの最後の要素からAの最初の要素までの距離よりも大きいということ
        # 例えばK = 6の場合、Aの最後の要素からAの最初の要素までの距離は5-1-1=3である
        # これはAの最後の要
