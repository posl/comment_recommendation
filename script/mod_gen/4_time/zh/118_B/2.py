def main():
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    cnt = [0] * M
    for i in range(N):
        for j in range(1, A[i][0] + 1):
            cnt[A[i][j] - 1] += 1
    ans = 0
    for i in range(M):
        if cnt[i] == N:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()