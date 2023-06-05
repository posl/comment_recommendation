def main():
    # 读取输入
    n, a, b = map(int, input().split())
    # 1到n之间的整数
    num = n
    # 不是a的倍数的整数
    num -= n // a
    # 不是b的倍数的整数
    num -= n // b
    # 不是a和b的倍数的整数
    num += n // (a * b // gcd(a, b))
    # 输出结果
    print(num)
