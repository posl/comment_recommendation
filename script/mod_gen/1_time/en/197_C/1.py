def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(A[0])
        return
    if N == 2:
        print(A[0] ^ A[1])
        return
    A.sort()
    A = [A[0]] + A
    B = [0] * (N + 1)
    B[1] = A[1]
    for i in range(2, N + 1):
        B[i] = B[i - 1] | A[i]
    C = [0] * (N + 1)
    C[N] = A[N]
    for i in range(N - 1, 0, -1):
        C[i] = C[i + 1] | A[i]
    ans = 10 ** 9
    for i in range(1, N):
        ans = min(ans, B[i] ^ C[i + 1])
    print(ans)

if __name__ == '__main__':
    solve()