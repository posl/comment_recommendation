def main():
    # 读取输入
    S = input()
    # 用集合去重
    S_set = set(S)
    # 集合中元素个数
    S_set_len = len(S_set)
    # 用数学公式计算排列组合
    result = S_set_len * (S_set_len - 1) * (S_set_len - 2)
    # 打印输出
    print(result)

if __name__ == '__main__':
    main()