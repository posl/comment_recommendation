def solve():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    #print(S)
    ans = 0
    for i1 in range(H):
        for j1 in range(W):
            for i2 in range(H):
                for j2 in range(W):
                    if i1 == i2 and j1 == j2:
                        continue
                    if S[i1][j1] == '#' or S[i2][j2] == '#':
                        continue
                    if i1 == i2:
                        ok = True
                        for j in range(min(j1,j2),max(j1,j2)+1):
                            if S[i1][j] == '#':
                                ok = False
                        if ok:
                            ans = max(ans,abs(j1-j2)+1)
                    if j1 == j2:
                        ok = True
                        for i in range(min(i1,i2),max(i1,i2)+1):
                            if S[i][j1] == '#':
                                ok = False
                        if ok:
                            ans = max(ans,abs(i1-i2)+1)
    print(ans)

if __name__ == '__main__':
    solve()