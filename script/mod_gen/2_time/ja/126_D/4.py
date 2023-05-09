def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        G[u-1].append((v-1, w))
        G[v-1].append((u-1, w))
    dp = [-1] * N
    dp[0] = 0
    stack = [0]
    while stack:
        i = stack.pop()
        for j, w in G[i]:
            if dp[j] == -1:
                dp[j] = dp[i] ^ (w % 2)
                stack.append(j)
    print(*dp, sep='
')

if __name__ == '__main__':
    main()