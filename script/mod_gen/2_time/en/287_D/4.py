def main():
    S = input()
    T = input()
    for x in range(len(T) + 1):
        S1 = S[:x]
        S2 = S[len(S) - len(T) + x:]
        S3 = S1 + S2
        if all(T[i] == S3[i] or T[i] == '?' or S3[i] == '?' for i in range(len(T))):
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()