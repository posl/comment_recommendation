def main():
    H, W, X, Y = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    
    X -= 1
    Y -= 1
    
    cnt = 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == '#': break
        cnt += 1
    for i in range(X+1, H):
        if S[i][Y] == '#': break
        cnt += 1
    for i in range(Y-1, -1, -1):
        if S[X][i] == '#': break
        cnt += 1
    for i in range(Y+1, W):
        if S[X][i] == '#': break
        cnt += 1
    print(cnt)
