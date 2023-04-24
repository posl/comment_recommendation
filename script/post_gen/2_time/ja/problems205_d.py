Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = []
    for i in range(Q):
        K.append(int(input()))
    #print(N, Q, A, K)

    # Aの最大値を求める
    max_A = max(A)

    # Aの最大値より大きい値を求める
    max_A_plus = 0
    for i in range(N):
        if max_A < A[i]:
            max_A_plus = A[i]
            break

    # Aの最大値より大きい値のindexを求める
    max_A_plus_index = 0
    for i in range(N):
        if max_A < A[i]:
            max_A_plus_index = i
            break

    # Aの最大値より大きい値を含めたリストを作成する
    A_plus = A[:max_A_plus_index] + [max_A_plus] + A[max_A_plus_index:]

    # Aの最大値より大きい値を含めたリストの累積和を求める
    A_plus_cumsum = [0]
    for i in range(len(A_plus)):
        A_plus_cumsum.append(A_plus_cumsum[i] + A_plus[i])

    #print(A_plus, A_plus_cumsum)

    # Kの値を使って、Aの最大値より大きい値を含めたリストの累積和の値を求める
    for i in range(Q):
        # Kの値がAの最大値より大きい場合
        if K[i] > max_A:
            # Aの最大値より大きい値のindexを求める
            max_A_plus_index = 0
            for j in range(N):
                if max_A < A[j]:
                    max_A_plus_index = j
                    break
            #print(max_A_plus_index)
            #print(A_plus_cumsum)
            print(A_plus_cumsum[max_A_plus_index] + (K[i] - max_A) * (N - max_A_plus_index))
        # Kの値

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]

    for k in K:
        left = 1
        right = 10**18
        while left <= right:
            mid = (left + right) // 2
            count = 0
            for a in A:
                count += mid // a
            if count >= k:
                right = mid - 1
            else:
                left = mid + 1
        print(left)

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A = [1] + A + [10**18]
    #print(A)
    for k in K:
        #print(k)
        left = 0
        right = N + 1
        while right - left > 1:
            mid = (left + right) // 2
            #print("mid", mid)
            if A[mid] - A[mid - 1] <= k:
                k -= A[mid] - A[mid - 1]
                left = mid
                #print("left", left)
            else:
                right = mid
                #print("right", right)
        print(A[left] + k - 1)

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]

    # 累積和を求める
    sumA = [0]
    for i in range(N):
        sumA.append(sumA[i] + A[i])

    # 二分探索で求める
    for k in K:
        # 二分探索でk番目の値を求める
        # 1, 2, 4, 8, 9, 10, 11, ... のうち k 番目の値を求める
        left = 0
        right = 10**18
        while right - left > 1:
            mid = (left + right) // 2
            # mid 以下の値の個数を求める
            # mid 以下の値の個数は mid 以下の値の累積和の個数
            cnt = 0
            for i in range(N):
                if A[i] <= mid:
                    cnt += 1
                else:
                    break
            # mid 以下の値の累積和
            sumMid = sumA[cnt]
            # mid 以下の値の個数が k 未満なら
            if sumMid < k:
                left = mid
            else:
                right = mid
        # k 番目の値
        ans = right
        # k 番目の値の個数は k 未満の値の個数
        cnt = 0
        for i in range(N):
            if A[i] < ans:
                cnt += 1
            else:
                break
        # k 番目の値の累積和
        sumAns = sumA[cnt]
        # k 番目の値の累積和が k 未満なら
        if sumAns < k:
            print(ans + k - sumAns)
        else:
            print(ans)

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]

    B = [0 for _ in range(N)]
    for i in range(N):
        B[i] = A[i] - (i + 1)

    for k in K:
        if k <= A[0]:
            print(k)
        elif k > A[-1]:
            print(A[-1] + k - N)
        else:
            ok = 0
            ng = N
            while ng - ok > 1:
                mid = (ok + ng) // 2
                if B[mid] < k:
                    ok = mid
                else:
                    ng = mid
            print(A[ok] + k - B[ok])

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]

    for k in K:
        print(binary_search(A, k))

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]

    # Aの最大値を求める
    max_A = max(A)

    # Aの最大値を超える最小の2のべき乗を求める
    # 例：max_A = 8の場合、2**3 = 8
    # 例：max_A = 9の場合、2**4 = 16
    max_pow = 1
    while max_pow <= max_A:
        max_pow *= 2

    # 2のべき乗の数列を求める
    # 例：max_pow = 8の場合、[1, 2, 4, 8]
    pow_list = [1]
    for _ in range(N):
        pow_list.append(pow_list[-1] * 2)

    # Aの要素を2のべき乗の数列の要素に変換する
    # 例：A = [3, 5, 6, 7]の場合、[2, 4, 8, 9]
    A = [pow_list.index(a) for a in A]

    # 2のべき乗の数列の累積和を求める
    # 例：pow_list = [1, 2, 4, 8]の場合、[1, 3, 7, 15]
    pow_list_sum = [0]
    for pow in pow_list:
        pow_list_sum.append(pow_list_sum[-1] + pow)

    # Aの要素を2のべき乗の数列の要素に変換したものの累積和を求める
    # 例：A = [2, 4, 8, 9]の場合、[0, 2, 6, 14, 23]
    A_sum = [0]
    for a in A:
        A_sum.append(A_sum[-1] + a)

    # クエリ毎に2のべ

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for i in range(Q)]

    #Aの最大値を求める
    maxA = A[-1]

    #Aの最小値を求める
    minA = A[0]

    #Aの最大値と最小値の差を求める
    diffA = maxA - minA

    #Aの最大値と最小値の差の2倍を求める
    diffA2 = diffA * 2

    #Aの最小値と最大値の差の2倍を求める
    diffA3 = diffA2 - 1

    #Aの最大値と最小値の差の2倍を求める
    diffA4 = diffA2 + 1

    #Aの最大値と最小値の差の2倍を求める
    diffA5 = diffA2 + 2

    #Aの最大値と最小値の差の2倍を求める
    diffA6 = diffA2 + 3

    #Aの最大値と最小値の差の2倍を求める
    diffA7 = diffA2 + 4

    #Aの最大値と最小値の差の2倍を求める
    diffA8 = diffA2 + 5

    #Aの最大値と最小値の差の2倍を求める
    diffA9 = diffA2 + 6

    #Aの最大値と最小値の差の2倍を求める
    diffA10 = diffA2 + 7

    #Aの最大値と最小値の差の2倍を求める
    diffA11 = diffA2 + 8

    #Aの最大値と最小値の差の2倍を求める
    diffA12 = diff

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]

    for i in range(Q):
        # リストの中にK[i]があればそのインデックスを返す
        if K[i] in A:
            print(K[i])
            continue
        # リストの中にK[i]がなければ、K[i]より大きい数の中で最小の数を返す
        # なければ、リストの中で最大の数を返す
        else:
            print(min([a for a in A if a > K[i]], default=max(A)))

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    #Aの最大値を取得
    maxA = max(A)
    #Aの最大値を超える数値を格納
    overA = []
    #Aの最大値を超える数値を格納
    for i in range(1, maxA + 1):
        if i not in A:
            overA.append(i)
    #Aの最大値を超える数値の個数を取得
    overA_num = len(overA)
    #Aの最大値を超える数値の個数がK以下の場合
    if overA_num <= K:
        print(overA_num)
    #Aの最大値を超える数値の個数がKより大きい場合
    else:
        print(K)
