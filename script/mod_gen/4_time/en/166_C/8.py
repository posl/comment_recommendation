def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    good = [1 for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        if h[a-1] <= h[b-1]:
            good[a-1] = 0
        if h[a-1] >= h[b-1]:
            good[b-1] = 0
    print(sum(good))
main()

if __name__ == '__main__':
    main()