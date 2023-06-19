def solution(H,W,coins):
    N = 0
    operation = []
    for i in range(H):
        for j in range(W):
            if coins[i][j] % 2 == 1:
                if j < W - 1:
                    coins[i][j] -= 1
                    coins[i][j+1] += 1
                    N += 1
                    operation.append([i+1,j+1,i+1,j+2])
                elif i < H - 1:
                    coins[i][j] -= 1
                    coins[i+1][j] += 1
                    N += 1
                    operation.append([i+1,j+1,i+2,j+1])
    print(N)
    for i in range(N):
        print(operation[i][0], operation[i][1], operation[i][2], operation[i][3])
