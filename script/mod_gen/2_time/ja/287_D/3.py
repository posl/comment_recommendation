def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[:i]
        S2 = S[len(S)-len(T)+i:]
        if S1+S2 == T.replace('?','a'):
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()