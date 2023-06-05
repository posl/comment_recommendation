def main():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))
    # 计算
    result = 0
    for i in A:
        if i > 10:
            result += i - 10
    # 打印输出
    print(result)
main()
