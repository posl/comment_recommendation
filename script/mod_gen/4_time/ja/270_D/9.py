def solve():
    # N K
    N, K = map(int, input().split())
    # A_1 A_2 ... A_K
    A = [int(i) for i in input().split()]
    # DP
    dp = [False] * (N+1)
    for i in range(N+1):
        for a in A:
            if i - a >= 0 and dp[i-a] == False:
                dp[i] = True
                break
    #print(dp)
    # calc
    ret = 0
    for i in range(N+1):
        if dp[i] == False:
            ret += 1
    print(ret)

if __name__ == '__main__':
    solve()