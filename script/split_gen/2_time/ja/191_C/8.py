def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    #print(S)
    #左から探索
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                left = j
                break
        if S[i][j] == "#":
            break
    #右から探索
    for i in range(H):
        for j in range(W-1, -1, -1):
            if S[i][j] == "#":
                right = j
                break
        if S[i][j] == "#":
            break
    #上から探索
    for i in range(W):
        for j in range(H):
            if S[j][i] == "#":
                up = j
                break
        if S[j][i] == "#":
            break
    #下から探索
    for i in range(W):
        for j in range(H-1, -1, -1):
            if S[j][i] == "#":
                down = j
                break
        if S[j][i] == "#":
            break
    #print(left, right, up, down)
    print(right-left+down-up+4)
