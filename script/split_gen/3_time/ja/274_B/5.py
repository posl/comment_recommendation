def main():
    H, W = map(int, input().split())
    C = [list(input()) for i in range(H)]
    #print(C)
    X = [0] * W
    for j in range(W):
        for i in range(H):
            if C[i][j] == "#":
                X[j] += 1
    print(*X)
