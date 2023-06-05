def main():
    # 读取输入
    A, B = map(int, input().split())
    # 用来计数的变量
    count = 0
    # 在这里写下你的代码
    for x in range(A, B + 1):
        if A <= x <= B:
            count += 1
    # 输出结果
    print(count)
