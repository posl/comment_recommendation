def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    #上下左右
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    #计数器
    cnt = 0
    #遍历
    for i in range(H):
        for j in range(W):
            #如果是黑色
            if S[i][j] == "#":
                #遍历上下左右
                for dx, dy in d:
                    #如果是白色
                    if 0 <= i+dx < H and 0 <= j+dy < W and S[i+dx][j+dy] == ".":
                        #计数器+1
                        cnt += 1
    #输出结果
    print(cnt)
