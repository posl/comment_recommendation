def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(N+1):
        B[0] += C[i] * A[i]
    for j in range(1, M+1):
        B[j] = (C[N+j] - B[0]) // A[0]
    print(*B)
    return 0

if __name__ == '__main__':
    solve()