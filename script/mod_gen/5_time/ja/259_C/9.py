def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        exit()
    if len(S) < len(T):
        print('No')
        exit()
    if len(S) == len(T):
        if S[0] == T[0] and S[1] == T[1]:
            print('Yes')
            exit()
        else:
            print('No')
            exit()
    else:
        if S[0] == T[0] and S[1] == T[1]:
            if S[2] == T[2]:
                print('Yes')
                exit()
            elif S[2] == S[1]:
                print('Yes')
                exit()
            else:
                print('No')
                exit()
        else:
            print('No')
            exit()

if __name__ == '__main__':
    main()