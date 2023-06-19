def main():
    S = input()
    T = input()
    if len(S) > len(T):
        print('No')
        return
    if S == T:
        print('Yes')
        return
    for i in range(len(S)):
        if S[i] != T[i]:
            if S[i+1:] == T[i+1:]:
                print('Yes')
                return
            else:
                print('No')
                return
    print('No')
main()
