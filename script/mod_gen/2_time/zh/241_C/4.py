def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        for j in range(N):
            if S[i][j] == '#':
                S[i][j] = 1
            else:
                S[i][j] = 0
    for i in range(N):
        for j in range(N):
            if S[i][j] == 1:
                for k in range(2, N):
                    if i + k < N and j + k < N and S[i + k][j] == 1 and S[i][j + k] == 1 and S[i + k][j + k] == 1:
                        print('Yes')
                        return
    print('No')

if __name__ == '__main__':
    main()