def main():
    A, B, K = map(int, input().split())
    if A == 0 or B == 0:
        print("a" * A + "b" * B)
        return
    # dp[a][b] = (a + b) C a
    dp = [[0] * (B + 1) for _ in range(A + 1)]
    dp[0][0] = 1
    for a in range(1, A + 1):
        dp[a][0] = 1
        for b in range(1, B + 1):
            dp[a][b] = dp[a - 1][b] + dp[a][b - 1]
    while A + B > 0:
        if A == 0:
            print("b", end="")
            B -= 1
            continue
        if B == 0:
            print("a", end="")
            A -= 1
            continue
        if K <= dp[A - 1][B]:
            print("a", end="")
            A -= 1
        else:
            print("b", end="")
            K -= dp[A - 1][B]
            B -= 1
    print()
