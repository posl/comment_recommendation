def main():
    S = input()
    N = len(S)
    for i in range(N):
        if S[i] != S[N-1-i]:
            if S[i] == 'a':
                print('Yes')
                return
            else:
                print('No')
                return
    print('Yes')
    return

if __name__ == '__main__':
    main()