def main():
    import sys
    read = sys.stdin.buffer.read
    N, M, *AB = map(int, read().split())
    if M == 0:
        print(3**N)
        return
    edge = [0] * N
    for a, b in zip(*(iter(AB),) * 2):
        edge[a - 1] |= 1 << (b - 1)
        edge[b - 1] |= 1 << (a - 1)
    dp = [0] * (1 << N)
    dp[0] = 1
    for i in range(1 << N):
        for j in range(N):
            if (i >> j) & 1:
                continue
            if i & edge[j] == 0:
                dp[i | (1 << j)] += dp[i]
    print(dp[-1] * 3)
