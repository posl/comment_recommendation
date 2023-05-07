def solve():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = min(max(A[i], L), R)
    print(sum(B))
solve()

if __name__ == '__main__':
    solve()