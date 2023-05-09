def main():
    # 配列の長さ
    N = int(input())
    # 配列を取得
    A = list(map(int, input().split()))
    # 答え
    ans = 0
    # 1個目の配列の要素を取得
    for i in range(N):
        # 2個目の配列の要素を取得
        for j in range(i + 1, N):
            # 答えに配列の要素を掛けたものを足す
            ans += A[i] * A[j]
    # 答えを出力
    print(ans % (10 ** 9 + 7))
