def check(S,T):
    if (len(S) < len(T)):
        return False
    for i in range(len(S) - len(T)+1):
        for j in range(len(T)):
            if (S[i+j] != T[j]):
                break
        else:
            return True
    return False

if __name__ == '__main__':
    check()