def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 1. A の要素を K 個ずつに分割する
    # 2. 分割した要素の中で最小値を求める
    # 3. 最小値を K 個の要素の中での最大値を求める
    # 4. 3. の最大値を求める
    # 5. 4. で求めた最大値を A の要素数で割った商が答え
    # 5. の商が 0 なら 1 にする
    ans = 0
    for i in range(0, N, K):
        ans = max(ans, min(A[i:i+K]))
    print((N - ans + K - 1) // K)

if __name__ == '__main__':
    main()