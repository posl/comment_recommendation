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

if __name__ == '__main__':
    main()