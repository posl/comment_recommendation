def main():
    # 標準入力の値を取得
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(Q)]
    # 二分探索を行うため、Aをソート
    A.sort()
    # xの値について、Aにおけるx以上の値の数を出力
    for i in range(Q):
        # 二分探索
        left = 0
        right = N
        while left < right:
            mid = (left + right) // 2
            if A[mid] >= x[i]:
                right = mid
            else:
                left = mid + 1
        print(N - left)

if __name__ == '__main__':
    main()