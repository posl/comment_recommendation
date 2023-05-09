def solve():
    X, N = map(int, input().split())
    if N == 0:
        return X
    p = list(map(int, input().split()))
    if X not in p:
        return X
    else:
        for i in range(1, 100):
            if X - i not in p:
                return X - i
            elif X + i not in p:
                return X + i

if __name__ == '__main__':
    solve()