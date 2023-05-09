def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                x, y = i, j
                break
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                print(abs(x - i) + abs(y - j))
                return
