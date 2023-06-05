def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                cnt += 1
    print(cnt)
