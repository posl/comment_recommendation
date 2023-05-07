def solve():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    good = [1] * N
    for a, b in AB:
        if H[a - 1] > H[b - 1]:
            good[b - 1] = 0
        elif H[a - 1] < H[b - 1]:
            good[a - 1] = 0
        else:
            good[a - 1] = 0
            good[b - 1] = 0
    print(sum(good))
