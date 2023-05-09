def main():
    # N, M = map(int, input().split())
    # a = list(map(int, input().split()))
    # c = list(map(int, input().split()))
    N, M = map(int, '1 1'.split())
    a = list(map(int, '100 1'.split()))
    c = list(map(int, '10000 0 -1'.split()))
    b = [0] * (M + 1)
    b[0] = c[0] // a[0]
    for i in range(1, M + 1):
        b[i] = (c[i] - sum([b[j] * a[i - j] for j in range(i)])) // a[0]
    print(' '.join(map(str, b)))

if __name__ == '__main__':
    main()