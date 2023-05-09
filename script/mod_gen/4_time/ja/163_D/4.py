def main():
    N, K = map(int, input().split())
    if K == 1:
        print(N+1)
    else:
        ans = 0
        for i in range(K, N+2):
            ans += (i*(N-i+1)+1)
        print(ans%1000000007)

if __name__ == '__main__':
    main()