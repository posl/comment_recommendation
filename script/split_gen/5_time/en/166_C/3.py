def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    if N == 1:
        print(1)
        return
    good = [True] * N
    for a, b in AB:
        if H[a - 1] <= H[b - 1]:
            good[a - 1] = False
        if H[b - 1] <= H[a - 1]:
            good[b - 1] = False
    print(good.count(True))
