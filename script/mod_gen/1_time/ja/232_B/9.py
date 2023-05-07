def main():
    S = input()
    T = input()
    if len(S) == len(T):
        for i in range(26):
            if S == T:
                print('Yes')
                exit()
            S = S[1:] + S[0]
    print('No')

if __name__ == '__main__':
    main()