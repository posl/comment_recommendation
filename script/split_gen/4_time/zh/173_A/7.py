def solve():
    # 请在此处添加代码，实现函数solve()，函数中不要使用input/output方法进行输入输出操作
    # 返回值：返回一个整数，表示结果
    n = int(input())
    if n < 1000:
        return 1000 - n
    else:
        return n % 1000
