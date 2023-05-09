def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)] # 2次元配列を入力するときはこのようにしておくと便利
    i = 0
    j = 0
    for _ in range(H*W):
        if G[i][j] == "U":
            if i != 0:
                i -= 1
            else:
                print(i+1, j+1)
                return
        elif G[i][j] == "D":
            if i != H-1:
                i += 1
            else:
                print(i+1, j+1)
                return
        elif G[i][j] == "L":
            if j != 0:
                j -= 1
            else:
                print(i+1, j+1)
                return
        elif G[i][j] == "R":
            if j != W-1:
                j += 1
            else:
                print(i+1, j+1)
                return
    print(-1)
