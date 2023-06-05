def main():
    H, W = map(int, input().split())
    C = [input() for i in range(H)]
    for i in range(H):
        count = 0
        for j in range(W):
            if C[i][j] == '#':
                count += 1
        print(count)
