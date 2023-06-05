def main():
    H, W = map(int, input().split())
    C = [input() for i in range(H)]
    for i in range(H):
        print(sum([1 if C[i][j] == "#" else 0 for j in range(W)]))
