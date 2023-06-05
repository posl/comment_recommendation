def main():
    S = input()
    T = input()
    if len(S) == len(T):
        for i in range(len(S)):
            if S[i] != T[i]:
                if S[i] in S[:i] or T[i] in T[:i]:
                    print('No')
                    break
                else:
                    S = S.replace(S[i], T[i])
                    T = T.replace(T[i], S[i])
        else:
            if S == T:
                print('Yes')
            else:
                print('No')
    else:
        print('No')
