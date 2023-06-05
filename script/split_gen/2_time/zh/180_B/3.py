def main():
    # 读取数据
    # 读取一行数据，然后按空格分割成一个列表
    # 读取的数据是字符串类型
    line = input().split(" ")
    # 将数据转换成整数类型
    N = int(line[0])
    A = int(line[1])
    B = int(line[2])
    # 计算答案
    ans = N - A + B
    # 打印答案
    print(ans)
