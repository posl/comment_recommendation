def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    count = 0
    #print(S)
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                count += 1
    print(count)
    return
