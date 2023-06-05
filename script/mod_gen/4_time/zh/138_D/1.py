def solve():
    N, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N-1)]
    B = [list(map(int, input().split())) for _ in range(Q)]
    C = [0] * N
    for b in B:
        C[b[0]-1] += b[1]
    for a in A:
        C[a[1]-1] += C[a[0]-1]
    print(*C)

if __name__ == '__main__':
    solve()