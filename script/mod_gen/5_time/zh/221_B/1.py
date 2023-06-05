def swap(S,T):
    if len(S) != len(T):
        return False
    if S == T:
        return True
    else:
        for i in range(len(S)):
            for j in range(i+1,len(S)):
                if S[i] == T[j] and S[j] == T[i]:
                    return True
    return False

if __name__ == '__main__':
    swap()