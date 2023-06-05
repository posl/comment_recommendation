def main():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)
    for x in range(T_len+1):
        S_ = S[:x] + S[S_len-(T_len-x):]
        if S_ == T:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()