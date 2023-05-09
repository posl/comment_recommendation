def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #print(S)
    ans = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for n in range(10):
                            for o in range(10):
                                for p in range(10):
                                    for q in range(10):
                                        for r in range(10):
                                            if (i == j and j == k and k == l and l == m and m == n and n == o and o == p and p == q and q == r):
                                                #print(i,j,k,l,m,n,o,p,q,r)
                                                #print(S[0][i],S[1][j],S[2][k],S[3][l],S[4][m],S[5][n],S[6][o],S[7][p],S[8][q],S[9][r])
                                                if (S[0][i] == S[1][j] and S[1][j] == S[2][k] and S[2][k] == S[3][l] and S[3][l] == S[4][m] and S[4][m] == S[5][n] and S[5][n] == S[6][o] and S[6][o] == S[7][p] and S[7][p] == S[8][q] and S[8][q] == S[9][r]):
                                                    #print(i,j,k,l,m,n,o,p,q,r)
                                                    #print(S[0][i],S[1][j],S[2][k],S[3][l],S[4][m],S[5][n],S[6][o],S[7][p],S[8][q],S[9][r])
                                                    ans = max(ans, i+j+k+l+m+n+o+p+q+r)
    print(ans)
