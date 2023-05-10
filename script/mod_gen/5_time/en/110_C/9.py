def check(S,T):
    if len(S) != len(T):
        return False
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        else:
            if S[i] in S[i+1:]:
                S = S.replace(S[i],T[i])
            else:
                return False
    return True
S = input()
T = input()

if __name__ == '__main__':
    check()