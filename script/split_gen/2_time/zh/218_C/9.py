def check(S,T):
    #print(S)
    #print(T)
    #print("-----------")
    for i in range(len(S)):
        for j in range(len(S)):
            if S[i][j] != T[i][j]:
                return False
    return True
