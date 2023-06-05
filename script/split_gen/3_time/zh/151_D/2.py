def main():
    H,W = map(int,input().split())
    S = [list(input()) for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                #print(i,j)
                #print(S[i][j])
                #print(S[i][j+1])
                #print(S[i][j-1])
                #print(S[i+1][j])
                #print(S[i-1][j])
                if i == 0:
                    if j == 0:
                        if S[i][j+1] == '.':
                            ans += 1
                        if S[i+1][j] == '.':
                            ans += 1
                    elif j == W-1:
                        if S[i][j-1] == '.':
                            ans += 1
                        if S[i+1][j] == '.':
                            ans += 1
                    else:
                        if S[i][j+1] == '.':
                            ans += 1
                        if S[i][j-1] == '.':
                            ans += 1
                        if S[i+1][j] == '.':
                            ans += 1
                elif i == H-1:
                    if j == 0:
                        if S[i][j+1] == '.':
                            ans += 1
                        if S[i-1][j] == '.':
                            ans += 1
                    elif j == W-1:
                        if S[i][j-1] == '.':
                            ans += 1
                        if S[i-1][j] == '.':
                            ans += 1
                    else:
                        if S[i][j+1] == '.':
                            ans += 1
                        if S[i][j-1] == '.':
                            ans += 1
                        if S[i-1][j] == '.':
                            ans += 1
                else:
                    if j == 0:
                        if S[i][j+1] == '.':
                            ans += 1
                        if S[i+1][j] == '.':
                            ans += 1
                        if S[i-1][j] == '.':
                            ans += 1
                    elif j == W-1:
                        if S[i][j-1] == '.':
                            ans +=
