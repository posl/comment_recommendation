def main():
    import sys
    from collections import deque
    def input(): return sys.stdin.readline().rstrip()
    N = int(input())
    T = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K = map(int, input().split())
        A[i] = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for i in range(N):
        for j in A[i]:
            G[j-1].append(i)
    dp = [0] * N
    dp[0] = T[0]
    for i in range(1, N):
        dp[i] = dp[i-1] + T[i]
        for j in G[i]:
            dp[i] = min(dp[i], dp[j-1] + T[i])
    print(dp[-1])

if __name__ == '__main__':
    main()