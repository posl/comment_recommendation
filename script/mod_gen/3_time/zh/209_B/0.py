def main():
    # 读入数据
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    # 计算
    sum = 0
    for i in range(N):
        if i % 2 == 0:
            sum += A[i]
        else:
            sum += A[i] - 1
    # 输出
    if sum <= X:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()