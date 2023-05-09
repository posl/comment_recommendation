def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        ans += (N // i) * max(0, i - K + 1)
        ans += max(0, (N % i) - K + 1)
    print(ans)

if __name__ == '__main__':
    main()