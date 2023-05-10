def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N - K + 1):
        ans = max(ans, sum(P[i:i + K]) / 2 + K / 2)
    print(ans)

if __name__ == '__main__':
    main()