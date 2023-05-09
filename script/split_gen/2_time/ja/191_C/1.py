def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    #print(S)
    n = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                n += 1
    print(n)
