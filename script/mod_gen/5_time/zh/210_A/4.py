def problems210_a():
    # 读取输入
    n, a, x, y = map(int, input().split())
    # 计算结果
    if n > a:
        result = a * x + (n - a) * y
    else:
        result = n * x
    # 输出结果
    print(result)

if __name__ == '__main__':
    problems210_a()