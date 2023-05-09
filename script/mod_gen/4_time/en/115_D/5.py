def level_burger(N, X):
    if N == 0:
        return 0
    elif X == 1:
        return 0
    elif X <= 1 + (2 ** (N + 1) - 3):
        return level_burger(N - 1, X - 1)
    else:
        return 2 ** N + level_burger(N - 1, X - 2 ** (N + 1) + 1)
N, X = map(int, input().split())
print(level_burger(N, X))

if __name__ == '__main__':
    level_burger()