def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if all(S[i][k] == 'o' or S[j][k] == 'o' for k in range(M)):
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()