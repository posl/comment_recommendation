def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(1, 2**N):
        count = 0
        sum = 0
        for j in range(N):
            if (i >> j) & 1:
                count += 1
                sum += A[j]
        if sum % count == 0:
            ans += 1
    print(ans % MOD)
