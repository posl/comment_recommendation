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

if __name__ == '__main__':
    solve()