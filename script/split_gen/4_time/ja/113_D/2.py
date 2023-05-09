def solve(H, W, K):
    if W == 1:
        return 1
    elif K == 1:
        return solve(H, W - 1, K) + solve(H, W - 1, K + 1)
    elif K == W:
        return solve(H, W - 1, K) + solve(H, W - 1, K - 1)
    else:
        return solve(H, W - 1, K - 1) + solve(H, W - 1, K) + solve(H, W - 1, K + 1)
