def main():
    # 读取输入
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    # 计算平均值
    average = sum(sum(A, [])) // (H * W)
    # 计算答案
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += abs(A[i][j] - average)
    # 输出答案
    print(ans)

if __name__ == '__main__':
    main()