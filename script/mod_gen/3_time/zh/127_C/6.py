def solve():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    L = max(L)
    R = min(R)
    if R - L + 1 < 0:
        return 0
    else:
        return R - L + 1

if __name__ == '__main__':
    solve()