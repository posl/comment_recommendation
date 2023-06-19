def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = sum(a) - 2 * sum(a[1::2])
    for i in range(1, n):
        b[i] = 2 * a[i - 1] - b[i - 1]
    print(*b)

if __name__ == '__main__':
    main()