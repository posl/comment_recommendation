def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    B[0] = C[0] // A[-1]
    for i in range(M + 1):
        for j in range(N):
            B[i] -= B[i - j - 1] * A[j]
        if i == M:
            break
        B[i + 1] = C[i + 1] // A[-1]
    print(' '.join(map(str, B)))

if __name__ == '__main__':
    solve()