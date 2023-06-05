def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2 * n + 1)
    for i in range(n):
        b[a[i]] = i + 1
    for i in range(1, 2 * n + 1):
        j = i
        while j <= 2 * n:
            b[j] = max(b[j], b[i] + 1)
            j += i
    for i in range(1, 2 * n + 1):
        print(b[i] - 1)

if __name__ == '__main__':
    main()