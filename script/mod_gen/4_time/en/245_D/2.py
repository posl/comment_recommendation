def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0] * (m + 1)
    for i in range(n + m):
        for j in range(m + 1):
            b[j] += c[i] * a[i - j]
    print(*b)

if __name__ == '__main__':
    main()