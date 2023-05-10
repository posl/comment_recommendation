def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        if S[i] == T[i]:
            print('No')
            exit()
    for i in range(N):
        if S[i] in T[i+1:]:
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()