def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print('No')
        return
    for i in range(len(S)):
        if S == T:
            print('Yes')
            return
        S = S[-1] + S[:-1]
    print('No')
main()
