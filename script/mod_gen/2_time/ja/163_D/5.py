def main():
    # input
    N, K = map(int, input().split())
    # compute
    ans = 0
    for i in range(K, N+2):
        ans += i*(N-i+1)+1
        ans %= 10**9+7
    # output
    print(ans)

if __name__ == '__main__':
    main()