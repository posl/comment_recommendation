def printString(S,K):
    if len(S) <= K:
        print(S)
    else:
        print(S[0:K]+'...')
