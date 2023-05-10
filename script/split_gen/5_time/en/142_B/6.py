def solve(N, K, heights):
    count = 0
    for h in heights:
        if h >= K:
            count += 1
    return count
