def main():
    # 读取输入
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # 处理
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    # 输出结果
    print(ans)
