def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S = [list(s) for s in S]
    T = [list(t) for t in T]
    for i in range(H):
        for j in range(W):
            if S[i][j] == T[i][j]:
                continue
            else:
                if S[i][j] == '#':
                    S[i][j] = '.'
                else:
                    S[i][j] = '#'
                if i == 0:
                    if j == 0:
                        if S[i][j+1] == '#':
                            S[i][j+1] = '.'
                        else:
                            S[i][j+1] = '#'
                        if S[i+1][j] == '#':
                            S[i+1][j] = '.'
                        else:
                            S[i+1][j] = '#'
                    elif j == W-1:
                        if S[i][j-1] == '#':
                            S[i][j-1] = '.'
                        else:
                            S[i][j-1] = '#'
                        if S[i+1][j] == '#':
                            S[i+1][j] = '.'
                        else:
                            S[i+1][j] = '#'
                    else:
                        if S[i][j+1] == '#':
                            S[i][j+1] = '.'
                        else:
                            S[i][j+1] = '#'
                        if S[i][j-1] == '#':
                            S[i][j-1] = '.'
                        else:
                            S[i][j-1] = '#'
                        if S[i+1][j] == '#':
                            S[i+1][j] = '.'
                        else:
                            S[i+1][j] = '#'
                elif i == H-1:
                    if j == 0:
                        if S[i][j+1] == '#':
                            S[i][j+1] = '.'
                        else:
                            S[i][j+1] = '#'
                        if S[i-1][j] == '#':
                            S[i-1][j] = '.'
                        else:
                            S[i-1][j] = '#'
                    elif j
