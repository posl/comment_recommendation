def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0] * (m + 1)
    for i in range(n + m, n, -1):
        b[m] = c[i]
        for j in range(n, -1, -1):
            c[j + m - n] -= a[j] * b[m]
        m -= 1
    print(" ".join(map(str, b)))

if __name__ == '__main__':
    main()