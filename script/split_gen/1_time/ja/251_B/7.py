def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    # おもりの重さの和がiになるようなおもりの組み合わせの数
    dp = [0] * (W + 1)
    dp[0] = 1
    for a in A:
        for i in range(W, a - 1, -1):
            dp[i] += dp[i - a]
    print(dp[W])
