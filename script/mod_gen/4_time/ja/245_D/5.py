def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M+1)
    for i in range(M+1):
        B[i] = C[N+M-i]
        for j in range(N+M-i):
            C[j] -= A[j] * B[i]
    print(*B)

if __name__ == '__main__':
    solve()