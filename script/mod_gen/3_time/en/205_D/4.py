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

if __name__ == '__main__':
    main()