def main():
    # input
    H, W = map(int, input().split())
    Ss = [list(input()) for _ in range(H)]
    # compute
    cnt = 0
    for i in range(H):
        for j in range(W):
            if Ss[i][j] == 'o':
                cnt += 1
    if cnt == 1:
        print(0)
        exit()
    # output
    print(cnt)
