def solve():
    # 读入数据
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]
    # print(S)
    # 初始化
    i, j = 0, 0
    # 无限循环
    while True:
        # 判断当前位置的字符
        if S[i][j] == 'U':
            # 如果是U，且i≠1，则移动到（i-1,j）。
            if i == 0:
                print(i+1, j+1)
                break
            else:
                i -= 1
        elif S[i][j] == 'D':
            # 如果是D，且i≠H，则移动到（i+1,j）。
            if i == H-1:
                print(i+1, j+1)
                break
            else:
                i += 1
        elif S[i][j] == 'L':
            # 如果是L且j≠1，则移动到（i,j-1）。
            if j == 0:
                print(i+1, j+1)
                break
            else:
                j -= 1
        elif S[i][j] == 'R':
            # 如果是R且j≠W，则移动到（i,j+1）。
            if j == W-1:
                print(i+1, j+1)
                break
            else:
                j += 1

if __name__ == '__main__':
    solve()