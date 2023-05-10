def lamp(H,W,S):
    #print(H,W,S)
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                #print(i,j)
                cnt = 1
                for k in range(j+1,W):
                    if S[i][k] == '#':
                        break
                    else:
                        cnt += 1
                for k in range(j-1,-1,-1):
                    if S[i][k] == '#':
                        break
                    else:
                        cnt += 1
                for k in range(i+1,H):
                    if S[k][j] == '#':
                        break
                    else:
                        cnt += 1
                for k in range(i-1,-1,-1):
                    if S[k][j] == '#':
                        break
