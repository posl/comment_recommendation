def solve(N,X,S):
    #print(N,X,S)
    #print(S)
    #print(N,X,S)
    for i in range(N):
        if S[i] == 'U':
            X = X//2
        elif S[i] == 'L':
            X = X*2-1
        else:
            X = X*2
    return X
