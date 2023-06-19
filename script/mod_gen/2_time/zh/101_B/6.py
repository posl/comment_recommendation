def main():
    # 读取输入
    N = int(input())
    # 计算S(N)
    S = 0
    for i in str(N):
        S += int(i)
    # 判断是否能够整除
    if N % S == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()