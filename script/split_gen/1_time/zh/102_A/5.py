def main():
    # 读取输入
    n = int(input())
    # 初始化结果
    result = 1
    # 循环
    while True:
        # 判断
        if result % n == 0 and result % 2 == 0:
            # 打印结果
            print(result)
            # 结束循环
            break
        # 结果+1
        result += 1
