def main():
    # 读取输入
    N = int(input())
    a = list(map(int, input().split()))
    # 操作次数
    count = 0
    # 重复操作
    while True:
        # 检查是否可以继续操作
        for i in range(N):
            if a[i] % 2 == 0:
                a[i] = a[i] // 2
            else:
                # 不能继续操作
                print(count)
                return
        # 操作次数加1
        count += 1

if __name__ == '__main__':
    main()