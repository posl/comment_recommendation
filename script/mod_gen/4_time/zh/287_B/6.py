def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    cnt = 0
    for i in range(M):
        for j in range(N):
            if S[j][3:] == T[i]:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()