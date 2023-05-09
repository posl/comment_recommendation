def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0 for i in range(m + 1)]
    for i in range(m, -1, -1):
        b[i] = c[i + n]
        for j in range(1, n + 1):
            b[i] -= a[j] * b[i + j]
        b[i] //= a[0]
    print(' '.join(map(str, b)))

if __name__ == '__main__':
    main()