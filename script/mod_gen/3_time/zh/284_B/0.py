def main():
    # 读取输入
    T = int(input())
    A = []
    for i in range(T):
        N = int(input())
        A.append(N)
        A.append(input().split())
    # 处理
    for i in range(T):
        count = 0
        for j in range(int(A[2*i])):
            if int(A[2*i+1][j]) % 2 == 1:
                count += 1
        # 输出结果
        print(count)

if __name__ == '__main__':
    main()