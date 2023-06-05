def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(M)]
    # print(N, M)
    # print(H)
    # print(ab)
    good = [True] * N
    for a, b in ab:
        if H[a-1] <= H[b-1]:
            good[a-1] = False
        if H[b-1] <= H[a-1]:
            good[b-1] = False
    print(good.count(True))

if __name__ == '__main__':
    main()