def solve(S,T):
    #print(S)
    #print(T)
    #print(len(S))
    #print(len(T))
    if len(S) < len(T):
        return False
    if S == T:
        return True
    if len(S) == len(T):
        return False
    if len(S) > len(T):
        if S[0:len(T)] == T:
            return True
        else:
            return solve(S[0:len(S)-1],T)

if __name__ == '__main__':
    solve()