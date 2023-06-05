def main():
    # 从标准输入读取数据
    N, A, B = map(int, input().split())
    # 计算答案
    ans = N - A + B
    # 打印答案
    print(ans)

if __name__ == '__main__':
    main()