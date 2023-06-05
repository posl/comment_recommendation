def main():
    N = int(input())
    MOD = 10**9+7
    dp = [0]*64
    for i in range(64):
        if i & 0b0111 == 0b0111:
            continue
        if i & 0b1001 == 0b1001:
            continue
        if i & 0b1100 == 0b1100:
            continue
        dp[i] = 1
    for i in range(N-3):
        dp2 = [0]*64
        for j in range(64):
            for k in range(4):
                dp2[(j<<1|k)&0b1111] += dp[j]
                dp2[(j<<1|k)&0b1111] %= MOD
        dp = dp2
    print(sum(dp)%MOD)

if __name__ == '__main__':
    main()