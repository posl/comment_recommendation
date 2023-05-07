def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    d = {}
    for i in range(N):
        if S[i] not in d:
            d[S[i]] = T[i]
        else:
            d[S[i]] = max(d[S[i]], T[i])
    for i in range(N):
        if T[i] == d[S[i]]:
            print(i+1)
            exit()

if __name__ == '__main__':
    main()