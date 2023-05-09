def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    # 累積和
    cumsum = [0]
    for i in range(N):
        cumsum.append(cumsum[i] + (p[i] + 1) / 2)
    ans = 0
    for i in range(N - K + 1):
        ans = max(ans, cumsum[i + K] - cumsum[i])
    print(ans)

if __name__ == '__main__':
    main()