def quiz(N,X,S):
    for i in range(N):
        if S[i] == 'x' and X > 0:
            X -= 1
        elif S[i] == 'o' and X < 200000:
            X += 1
    return X
