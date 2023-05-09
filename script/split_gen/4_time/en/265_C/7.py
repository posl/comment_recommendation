def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    # print(H, W)
    # print(G)
    i = 0
    j = 0
    while True:
        if G[i][j] == 'U' and i != 0:
            i -= 1
        elif G[i][j] == 'D' and i != H-1:
            i += 1
        elif G[i][j] == 'L' and j != 0:
            j -= 1
        elif G[i][j] == 'R' and j != W-1:
            j += 1
        else:
            break
    print(i+1, j+1)
main()
