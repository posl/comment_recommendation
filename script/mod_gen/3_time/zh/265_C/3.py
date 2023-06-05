def main():
    H,W = map(int,input().split())
    G = [input() for _ in range(H)]
    i = j = 0
    visited = [[0]*W for _ in range(H)]
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
        if visited[i][j] == 1:
            print(-1)
            return
        visited[i][j] = 1
    print(i+1,j+1)

if __name__ == '__main__':
    main()