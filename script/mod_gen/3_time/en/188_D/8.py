def main():
    N, C = map(int, input().split())
    # a_i, b_i, c_i
    service = [list(map(int, input().split())) for _ in range(N)]
    service.sort(key=lambda x: x[1])
    #print(service)
    # 1-indexed
    dp = [0] * (10**9+1)
    for i in range(N):
        a, b, c = service[i]
        dp[a] += c
        dp[b+1] -= c
    for i in range(1, 10**9+1):
        dp[i] += dp[i-1]
    ans = min([x * C for x in dp])
    print(ans)

if __name__ == '__main__':
    main()