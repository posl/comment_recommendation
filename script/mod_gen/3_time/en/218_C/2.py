def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        T.append(input())
    for i in range(N):
        for j in range(N):
            if S[i][j] == '#':
                s0 = i
                s1 = j
                break
    for i in range(N):
        for j in range(N):
            if T[i][j] == '#':
                t0 = i
                t1 = j
                break
    for i in range(N):
        for j in range(N):
            if S[s0+i][s1+j] != T[t0+i][t1+j]:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()