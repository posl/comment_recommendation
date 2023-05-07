def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(1,2**N):
        s = 0
        for j in range(N):
            if (i >> j) & 1:
                s += A[j]
        if s % bin(i).count('1') == 0:
            ans += 1
    print(ans % MOD)

if __name__ == '__main__':
    main()