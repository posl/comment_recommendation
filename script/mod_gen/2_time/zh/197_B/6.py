def main():
    #读取输入
    H, W, X, Y = map(int, input().split())
    S = [input() for i in range(H)]
    #初始化
    X -= 1
    Y -= 1
    #计算
    ans = 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == '.':
            ans += 1
        else:
            break
    for i in range(X+1, H):
        if S[i][Y] == '.':
            ans += 1
        else:
            break
    for i in range(Y-1, -1, -1):
        if S[X][i] == '.':
            ans += 1
        else:
            break
    for i in range(Y+1, W):
        if S[X][i] == '.':
            ans += 1
        else:
            break
    #输出
    print(ans)

if __name__ == '__main__':
    main()