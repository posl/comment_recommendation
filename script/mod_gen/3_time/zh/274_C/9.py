def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2 * n + 1)
    for i in range(n):
        b[a[i]] = i + 1
    c = [0] * (2 * n + 1)
    for i in range(2 * n, 0, -1):
        if i * 2 + 1 <= 2 * n:
            c[i] = max(c[i * 2], c[i * 2 + 1]) + 1
        elif i * 2 <= 2 * n:
            c[i] = c[i * 2] + 1
    for i in range(1, 2 * n + 1):
        print(c[1] - c[i])

if __name__ == '__main__':
    main()