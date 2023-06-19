def main():
    # 读取输入
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # 计算答案
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    # 打印输出
    print(ans)
main()
