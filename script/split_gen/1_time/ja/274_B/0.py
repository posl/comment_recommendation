def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    X = [0] * W
    for j in range(W):
        for i in range(H):
            if C[i][j] == '#':
                X[j] += 1
    print(*X)
