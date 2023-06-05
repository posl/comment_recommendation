def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N+1):
        ans += (N//a) * max(0, a-K)
        ans += max(0, (N%a) - K + 1)
        if K == 0:
            ans -= 1
    print(ans)

if __name__ == '__main__':
    main()