def main():
    # 读入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 处理
    # 1. 计算a中最大的值
    max_a = max(a)
    # 2. 计算max_a的位数
    max_a_len = len(bin(max_a)) - 2
    # 3. 如果k的位数小于max_a的位数，则k的位数扩展到max_a的位数
    if len(bin(k)) - 2 < max_a_len:
        k = k | (2 ** max_a_len - 1)
    # 4. 计算k的二进制表示
    k_bin = bin(k)[2:]
    # 5. 计算a中每个数的二进制表示
    a_bin = [bin(ai)[2:] for ai in a]
    # 6. 计算f(x)
    f = 0
    for i in range(max_a_len):
        # 6.1 计算a中每个数的第i位的1的个数
        one_num = 0
        for a_bin_i in a_bin:
            if len(a_bin_i) >= max_a_len - i and a_bin_i[max_a_len - i - 1] == '1':
                one_num += 1
        # 6.2 计算k的第i位的1的个数
        if len(k_bin) >= max_a_len - i and k_bin[max_a_len - i - 1] == '1':
            k_one_num = one_num
        else:
            k_one_num = n - one_num
        # 6.3 计算f(x)
        if k_one_num >= one_num:
            f += (2 ** (max_a_len - i - 1)) * one_num
        else:
            f += (2 ** (max_a_len - i - 1)) * (n - one_num)
    # 输出
    print(f)

if __name__ == '__main__':
    main()