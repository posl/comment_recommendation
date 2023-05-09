def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        return
    for i in range(len(S) - 1):
        if S[i] == T[i + 1] and T[i] == S[i + 1]:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()