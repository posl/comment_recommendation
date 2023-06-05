def main():
    #输入
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    #处理
    #从B的第一行开始，逐行检查
    for i in range(N):
        #计算B的第一行和A的第一行之间的差值
        diff = B[i][0] - (i * 7 + 1)
        #检查B的第一列和A的第一列之间的差值是否和diff一致
        for j in range(M):
            if B[i][j] - (i * 7 + j + 1) != diff:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()