def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    good = [True] * N
    for i in range(M):
        A, B = map(int, input().split())
        if H[A - 1] <= H[B - 1]:
            good[A - 1] = False
        if H[B - 1] <= H[A - 1]:
            good[B - 1] = False
    print(good.count(True))
main()
