def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    MOD = 998244353
    ans = 0
    for i in range(N):
        ans = (ans + (A[i] * pow(2, i, MOD)) % MOD) % MOD
    print(ans)

if __name__ == '__main__':
    main()