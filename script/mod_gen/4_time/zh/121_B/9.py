def solve():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        total = 0
        for j in range(M):
            total += A[i][j]*B[j]
        total += C
        if total > 0:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()