def main():
    # 读取输入
    N = int(input())
    # 读取输入
    N = int(input())
    # 将数字转换为字符串
    N_str = str(N)
    # 计算数字长度
    N_len = len(N_str)
    # 计算最大的乘积
    max_product = 0
    # 遍历所有的可能
    for i in range(1, N_len):
        # 将数字分为两个数字
        N_1 = int(N_str[:i])
        N_2 = int(N_str[i:])
        # 计算乘积
        product = N_1 * N_2
        # 更新最大值
        if product > max_product:
            max_product = product
    # 打印最大乘积
    print(max_product)
