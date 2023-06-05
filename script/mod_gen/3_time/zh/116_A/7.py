def main():
    # 从标准输入中读取
    # 读取的是字符串
    # 用空格分割字符串
    # 用map函数转换成整数
    # 用list函数转换成列表
    # 用tuple函数转换成元组
    # 用变量接收元组中的整数
    # 用算术表达式计算面积
    # 用print函数打印输出
    a, b, c = tuple(map(int, input().split()))
    print(int(a * b * 0.5))

if __name__ == '__main__':
    main()