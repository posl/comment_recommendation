def main():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)
    S = S.replace('?','a')
    T = T.replace('?','a')
    for i in range(S_len-T_len+1):
        if S[i:i+T_len] == T:
            print('Yes')
            for j in range(T_len):
                if S[i+j] == '?':
                    print('a')
                else:
                    print(S[i+j])
            for j in range(i+T_len,S_len):
                if S[j] == '?':
                    print('a')
                else:
                    print(S[j])
            break
        elif i == S_len-T_len:
            print('No')

if __name__ == '__main__':
    main()