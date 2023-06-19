def main():
    # 输入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 计算a中所有元素的最大位数
    max_bit = len(bin(max(a))) - 2
    # 计算a中所有元素的二进制表示
    a_bin = [[0] * n for _ in range(max_bit)]
    for i in range(n):
        for j in range(max_bit):
            a_bin[j][i] = (a[i] >> j) & 1
    # 计算a中所有元素的二进制表示的前缀和
    a_bin_cum = [[0] * (n + 1) for _ in range(max_bit)]
    for i in range(max_bit):
        for j in range(n):
            a_bin_cum[i][j + 1] = a_bin_cum[i][j] + a_bin[i][j]
    # 计算a中所有元素的二进制表示的前缀和的最大值
    a_bin_cum_max = [0] * max_bit
    for i in range(max_bit):
        a_bin_cum_max[i] = max(a_bin_cum[i])
    # 计算a中所有元素的二进制表示的前缀和的最大值的二进制表示
    a_bin_cum_max_bin = [0] * max_bit
    for i in range(max_bit):
        a_bin_cum_max_bin[i] = (a_bin_cum_max[i] >> i) & 1
    # 计算a中所有元素的二进制表示的前缀和的最大值的二进制表示的前缀和
    a_bin_cum_max_bin_cum = [0] * (max_bit + 1)
    for i in range(max_bit):
        a_bin_cum_max_bin_cum[i + 1] = a_bin_cum_max_bin_cum[i] + a_bin_cum_max_bin[i]
    # 计算a中所有元素的二进制表示的前缀和的最大值的二进制表示的前缀和的最大值
    a_bin_cum_max_bin_cum_max = max(a_bin_cum_max_bin_cum)
    # 计算a中所有元素
