def main():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))
    # 处理
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 != 0 and A[i] % 5 != 0:
                print('DENIED')
                exit()
    # 输出结果
    print('APPROVED')

if __name__ == '__main__':
    main()