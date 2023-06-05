def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    # W以下の正整数のうち、good integerであるものの個数を数える
    # 重さの小さい順にソートする
    A.sort()
    # dp[i] := 重さiを作るのに使うことができる最小の砝码の個数
    dp = [float('inf')] * (W + 1)
    # 重さ0は作れる
    dp[0] = 0
    for i in range(N):
        for w in range(W + 1):
            if w - A[i] >= 0:
                dp[w] = min(dp[w], dp[w - A[i]] + 1)
    print(dp[W])

if __name__ == '__main__':
    main()