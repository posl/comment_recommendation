def main():
    S = input()
    T = input()
    i = 0
    j = 0
    while i < len(S):
        if j == len(T):
            print('No')
            return
        if S[i] == T[j]:
            i += 1
        j += 1
    print('Yes')

if __name__ == '__main__':
    main()