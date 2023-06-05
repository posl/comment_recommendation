def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(m)]
    good = [True] * n
    for a, b in ab:
        if h[a - 1] < h[b - 1]:
            good[a - 1] = False
        elif h[a - 1] > h[b - 1]:
            good[b - 1] = False
        else:
            good[a - 1] = False
            good[b - 1] = False
    print(sum(good))

if __name__ == '__main__':
    main()