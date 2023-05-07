def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    print(sum([S[i][j] == '#' for i in range(H) for j in range(W)]))
