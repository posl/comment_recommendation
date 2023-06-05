def solve():
    # 读入数据
    N = int(input())
    A = list(map(int, input().split()))
    # 计算答案
    ans = 0
    for i in range(60):
        # 计算第i位的答案
        # 令c0为第i位为0的A的个数，c1为第i位为1的A的个数
        c0 = 0
        c1 = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                c1 += 1
            else:
                c0 += 1
        # 第i位的答案为c0 * c1 * 2^i
        ans += c0 * c1 * (1 << i)
        ans %= 10**9 + 7
    # 打印答案
    print(ans)

if __name__ == '__main__':
    solve()