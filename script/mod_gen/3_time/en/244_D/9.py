def main():
    #input
    S = input().split()
    T = input().split()
    #compute
    #output
    if S == T:
        print('Yes')
    elif S[0] == T[0] and S[1] == T[1] or S[1] == T[0] and S[2] == T[1] or S[2] == T[0] and S[0] == T[1] or S[0] == T[1] and S[1] == T[0] or S[1] == T[1] and S[2] == T[0] or S[2] == T[1] and S[0] == T[0]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()