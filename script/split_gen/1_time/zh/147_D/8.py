def main():
    from sys import stdin
    readline = stdin.readline
    N = int(readline())
    A = list(map(int, readline().split()))
    MOD = 10**9 + 7
    # 二进制表示的各位上的1的个数
    bit1 = [0] * 60
    for a in A:
        for i in range(60):
            bit1[i] += a >> i & 1
    ans = 0
    for i in range(60):
        # 2^i位上的1的个数
        n = bit1[i]
        # 2^i位上的1的个数 * 2^(N-1-i)个数
        ans += n * (N - n) * pow(2, i, MOD)
        ans %= MOD
    print(ans)
