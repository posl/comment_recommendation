def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        S[i] = list(S[i])
    for i in range(N):
        for j in range(N):
            if S[i][j] == '.':
                S[i][j] = 0
            else:
                S[i][j] = 1
    for i in range(N):
        for j in range(N-2):
            if S[i][j] == 1 and S[i][j+1] == 1 and S[i][j+2] == 1:
                print('Yes')
                return
    for j in range(N):
        for i in range(N-2):
            if S[i][j] == 1 and S[i+1][j] == 1 and S[i+2][j] == 1:
                print('Yes')
                return
    for i in range(N-2):
        for j in range(N-2):
            if S[i][j] == 1 and S[i+1][j+1] == 1 and S[i+2][j+2] == 1:
                print('Yes')
                return
    for i in range(2,N):
        for j in range(N-2):
            if S[i][j] == 1 and S[i-1][j+1] == 1 and S[i-2][j+2] == 1:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()