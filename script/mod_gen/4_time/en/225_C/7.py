def f():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    C = [B[0][j] % 7 for j in range(M)]
    for i in range(1, N):
        for j in range(M):
            if B[i][j] % 7 != C[j]:
                return 'No'
    return 'Yes'

if __name__ == '__main__':
    f()