def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    # 1. 二分探索
    # 2. 二分探索の回数を減らすために、探索範囲を小さくする
    # 3. 二分探索の結果をもとに、答えを求める
    # 4. 二分探索の結果は、Kより小さい数の個数
    # 5. Kより小さい数の個数は、K以下の数の個数 - Kと等しい数の個数
    # 6. K以下の数の個数は、二分探索の結果 + 1
    # 7. Kと等しい数の個数は、二分探索の結果の要素の個数
    # 1. 二分探索
    def binary_search(left, right, key):
        while left < right:
            mid = (left + right) // 2
            if A[mid] < key:
                left = mid + 1
            else:
                right = mid
        return left
    # 2. 二分探索の回数を減らすために、探索範囲を小さくする
    # 3. 二分探索の結果をもとに、答えを求める
    for k in K:
        # 2. 二分探索の回数を減らすために、探索範囲を小さくする
        # 5. K以下の数の個数は、二分探索の結果 + 1
        # 6. Kと等しい数の個数は、二分探索の結果の要素の個数
        ans = binary_search(0, N, k) + 1 + (A[binary_search(0
