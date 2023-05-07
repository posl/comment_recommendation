def main():
    #input
    H,W = map(int,input().split())
    S = [input() for i in range(H)]
    #solve
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    #output
    print(ans)
