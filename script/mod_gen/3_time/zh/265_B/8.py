def can_go(N, M, T, A, XY):
    xy = sorted(XY, key=lambda x: x[0])
    xy.append([N, 0])
    now = 1
    for x, y in xy:
        T -= x - now
        if T <= 0:
            return False
        T += y
        now = x
    return T >= N - now
N, M, T = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(M)]
print('Yes' if can_go(N, M, T, A, XY) else 'No')
