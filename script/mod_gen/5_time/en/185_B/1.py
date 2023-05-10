def solve():
    N, M, T = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    battery = N
    last = 0
    for i in range(M):
        battery -= A[i] - last
        if battery <= 0:
            return False
        battery += B[i] - A[i]
        if battery > N:
            battery = N
        last = B[i]
    battery -= T - last
    return battery > 0
print('Yes' if solve() else 'No')

if __name__ == '__main__':
    solve()