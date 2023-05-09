def main():
    S = input()
    if len(S) == 1:
        if int(S) % 8 == 0:
            print('Yes')
        else:
            print('No')
    elif len(S) == 2:
        if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
    else:
        S = list(S)
        S.sort()
        for i in range(len(S)):
            for j in range(len(S)):
                for k in range(len(S)):
                    if i != j and j != k and k != i:
                        if (int(S[i] + S[j] + S[k])) % 8 == 0:
                            print('Yes')
                            exit()
        print('No')

if __name__ == '__main__':
    main()