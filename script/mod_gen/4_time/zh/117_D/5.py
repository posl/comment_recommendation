def main():
    # 读入数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 生成前缀和
    sum_a = [0] * (n + 1)
    for i in range(n):
        sum_a[i + 1] = sum_a[i] + a[i]
    # 生成前缀和的二进制表示
    sum_a_bin = [0] * (n + 1)
    for i in range(n + 1):
        sum_a_bin[i] = bin(sum_a[i])[2:]
    sum_a_bin = list(map(list, sum_a_bin))
    # 生成前缀和的二进制表示的最大长度
    len_max = max(len(x) for x in sum_a_bin)
    # 生成前缀和的二进制表示的最大长度的二进制表示
    len_max_bin = bin(len_max)[2:]
    len_max_bin = list(len_max_bin)
    # 生成前缀和的二进制表示的最大长度的二进制表示的最大长度
    len_len_max = len(len_max_bin)
    # 生成前缀和的二进制表示的最大长度的二进制表示的最大长度的二进制表示
    len_len_max_bin = bin(len_len_max)[2:]
    len_len_max_bin = list(len_len_max_bin)
    # 生成前缀和的二进制表示的最大长度的二进制表示的最大长度的二进制表示的最大长度
    len_len_len_max = len(len_len_max_bin)
    # 生成前缀和的二进制表示的最大长度的二进制表示的最大长度的二进制表示的最大长度的二进制表示
    len_len_len_max_bin = bin(len_len_len_max)[2:]
    len_len_len_max_bin = list(len_len_len_max_bin)
    # 生成前缀和的二进制表示的最大长度的二进制表示的最大长度的二进制表示的最大长度的二进制表示的最大长度
    len_len_len_len_max = len(len_len_len_max_bin)
    # 生成前缀

if __name__ == '__main__':
    main()