def find_inserted_char(S, T):
    #print(S)
    #print(T)
    S = list(S)
    T = list(T)
    for i in range(len(S)):
        if S[i] != T[i]:
            return i+1
    return len(S)+1
