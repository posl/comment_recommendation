def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M+1)
    for i in range(M+1):
        B[i] = C[N+M-i] // A[N]
        for j in range(N+1):
            C[j+M-i] -= B[i] * A[j]
    print(*B)

if __name__ == '__main__':
    solve()