def burger(N, X):
    if N == 0:
        return 1 if X > 0 else 0
    if X == 1:
        return 0
    L = 2 ** (N + 1) - 3
    if X <= L // 2 + 1:
        return burger(N - 1, X - 1)
    if X == L // 2 + 2:
        return 2 ** (N - 1)
    return 2 ** (N - 1) + burger(N - 1, X - L // 2 - 2)
N, X = map(int, input().split())
print(burger(N, X))

if __name__ == '__main__':
    burger()