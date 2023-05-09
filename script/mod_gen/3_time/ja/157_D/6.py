def main():
    N, M, K = map(int, input().split())
    relation = [[0] * N for _ in range(N)]
    block = [[0] * N for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        relation[A - 1][B - 1] = 1
        relation[B - 1][A - 1] = 1
    for _ in range(K):
        C, D = map(int, input().split())
        block[C - 1][D - 1] = 1
        block[D - 1][C - 1] = 1
    ans = [0] * N
    for i in range(N):
        for j in range(N):
            if relation[i][j] == 1:
                ans[i] += 1
                ans[j] += 1
    for i in range(N):
        for j in range(N):
            if block[i][j] == 1:
                ans[i] -= 1
                ans[j] -= 1
    for i in range(N):
        ans[i] -= 1
    print(*ans)

if __name__ == '__main__':
    main()