def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(1, N+1):
        for j in range(2**N):
            if bin(j).count("1") == i:
                tmp = 0
                for k in range(N):
                    if (j >> k) & 1:
                        tmp += A[k]
                if tmp % i == 0:
                    ans += 1
    print(ans % MOD)

if __name__ == '__main__':
    main()