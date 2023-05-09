def main():
    import sys
    from collections import defaultdict
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    N, M = map(int, readline().split())
    A = list(map(int, read().split()))
    A.append(N)
    A.append(0)
    A.sort()
    #print(A)
    #print(N,M)
    dp = [0] * (N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,N+1):
        if i in A:
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 1000000007
    print(dp[-1])
    return
