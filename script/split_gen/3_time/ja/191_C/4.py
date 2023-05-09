def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    #print(S)
    #print(H, W)
    #print(S[0][0])
    
    #左上から黒マスを探す
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                #print(i, j)
                break
        if S[i][j] == '#':
            break
    
    #print(i, j)
    
    #左上から黒マスを探す
    for k in range(H):
        for l in range(W):
            if S[H-k-1][W-l-1] == '#':
                #print(i, j)
                break
        if S[H-k-1][W-l-1] == '#':
            break
    
    #print(H-k-1, W-l-1)
    
    #左上から黒マスを探す
    for m in range(H):
        for n in range(W):
            if S[m][W-n-1] == '#':
                #print(i, j)
                break
        if S[m][W-n-1] == '#':
            break
    
    #print(m, W-n-1)
    
    #左上から黒マスを探す
    for o in range(H):
        for p in range(W):
            if S[H-o-1][p] == '#':
                #print(i, j)
                break
        if S[H-o-1][p] == '#':
            break
    
    #print(H-o-1, p)
    
    #print(i, j, H-k-1, W-l-1, m, W-n-1, H-o-1, p)
    
    #print(i, j, H-k-1, W-l-1, m, W-n-1, H-o-1, p)
    #if i == H-k-1 and j == W-l-1:
    #    print(1)
    #elif i == H-k-1 and j == W-n-1:
    #    print(1)
    #elif i == H-o-1 and j == W-l-1:
    #    print(1)
