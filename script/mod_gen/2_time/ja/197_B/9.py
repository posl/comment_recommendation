def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for i in range(H)]
    #print(H, W, X, Y)
    #print(S)
    #print(S[X-1][Y-1])
    
    count = 0
    for i in range(X-1, -1, -1):
        if S[i][Y-1] == "#":
            break
        count += 1
    for i in range(X, H):
        if S[i][Y-1] == "#":
            break
        count += 1
    for i in range(Y-1, -1, -1):
        if S[X-1][i] == "#":
            break
        count += 1
    for i in range(Y, W):
        if S[X-1][i] == "#":
            break
        count += 1
    
    print(count)

if __name__ == '__main__':
    main()