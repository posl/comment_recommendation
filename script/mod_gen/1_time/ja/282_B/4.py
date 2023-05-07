def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    cnt = 0
    for i in range(N-1):
        for j in range(i+1,N):
            for k in range(M):
                if S[i][k] == 'o' or S[j][k] == 'o':
                    cnt += 1
                    break
    print(cnt)

if __name__ == '__main__':
    main()