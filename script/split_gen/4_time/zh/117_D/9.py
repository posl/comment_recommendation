def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 求出A中最大的数的位数，用于后面的循环
    max_bit = len(bin(max(A))) - 2
    # 用于记录每一位1的个数
    bit_count = [0] * max_bit
    for i in range(N):
        for j in range(max_bit):
            # 统计每一位1的个数
            if A[i] >> j & 1:
                bit_count[j] += 1
    # 从最高位开始，如果1的个数小于等于0的个数，则不改变原数的这一位，否则改为0
    # 这样可以保证得到的数一定小于等于K
    ans = 0
    for i in range(max_bit - 1, -1, -1):
        if bit_count[i] <= N // 2 and ans + (1 << i) <= K:
            ans += 1 << i
    # 计算最终的结果
    res = 0
    for i in range(N):
        res += ans ^ A[i]
    print(res)
