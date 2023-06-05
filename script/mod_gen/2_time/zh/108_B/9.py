def get_even_odd_method(k):
    # 偶数的个数
    even_num = k // 2
    # 奇数的个数
    odd_num = k - even_num
    # 选择偶数的方法
    even_method = even_num * odd_num
    return even_method

if __name__ == '__main__':
    get_even_odd_method()