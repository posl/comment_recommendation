def main():
    # 读取输入
    S = input()
    # 按照x分割字符串
    a, b = S.split('x')
    # 计算乘积
    ans = int(a) * int(b)
    # 打印结果
    print(ans)
main()
