def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        a, b = map(int, input().split())
        S.append([a, b])
    for i in range(N):
        c, d = map(int, input().split())
        T.append([c, d])
    S.sort()
    T.sort()
    for i in range(N):
        for j in range(N):
            x = T[j][0] - S[i][0]
            y = T[j][1] - S[i][1]
            S1 = []
            for k in range(N):
                S1.append([S[k][0] + x, S[k][1] + y])
            S1.sort()
            if S1 == T:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()