def check(S, T):
    S1 = []
    T1 = []
    for i in range(len(S)):
        S1.append(S[i])
        T1.append(T[i])
    S1.sort()
    T1.sort()
    if S1 == T1:
        return True
    else:
        return False

if __name__ == '__main__':
    check()