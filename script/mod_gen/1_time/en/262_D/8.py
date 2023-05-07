def main():
    def solve():
        mod = 998244353
        N = int(input())
        A = list(map(int, input().split()))
        ans = pow(2, N, mod) - 1
        for i in range(N):
            ans = (ans - pow(2, i, mod) * pow(2, N - i - 1, mod) * (N - i) * A[i]) % mod
        print(ans)
    solve()

if __name__ == '__main__':
    main()