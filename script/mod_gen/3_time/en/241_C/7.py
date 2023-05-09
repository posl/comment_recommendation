def main():
    N = int(input())
    S = [input() for _ in range(N)]
    #print(S)
    #check horizontally
    for i in range(N):
        cnt = 0
        for j in range(N):
            if S[i][j] == '.':
                cnt += 1
            else:
                cnt = 0
            if cnt >= 6:
                print('Yes')
                return
    #check vertically
    for i in range(N):
        cnt = 0
        for j in range(N):
            if S[j][i] == '.':
                cnt += 1
            else:
                cnt = 0
            if cnt >= 6:
                print('Yes')
                return
    #check diagonally
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i+j < N and S[j][i+j] == '.':
                cnt += 1
            else:
                cnt = 0
            if cnt >= 6:
                print('Yes')
                return
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i-j >= 0 and S[j][i-j] == '.':
                cnt += 1
            else:
                cnt = 0
            if cnt >= 6:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()