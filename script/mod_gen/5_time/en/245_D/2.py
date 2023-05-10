def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0] * (m + 1)
    for i in range(n + m):
        for j in range(min(i + 1, n)):
            b[i - j] += a[n - j - 1] * c[i]
    print(*b)

if __name__ == '__main__':
    main()