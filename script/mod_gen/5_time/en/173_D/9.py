def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    A.append(0)
    #print(N)
    #print(A)
    # dp[i]: i番目までのプレイヤーが到着した時点での、最大の快適度
    dp = [0]*(N+2)
    for i in range(1, N+2):
        dp[i] = max(dp[i-1], dp[i-2] + abs(A[i] - A[i-2]))
    print(dp[N+1])
main()

if __name__ == '__main__':
    main()