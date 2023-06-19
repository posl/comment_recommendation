def main():
    # 读取输入
    line = input()
    # 解析输入
    N, A, B = line.split(' ')
    N = int(N)
    A = int(A)
    B = int(B)
    # 计算答案
    ans = N + B - A
    # 打印答案
    print(ans)

if __name__ == '__main__':
    main()