def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - (i + 1)
    b.sort()
    if n % 2 == 0:
        print(b[n // 2] - b[n // 2 - 1] + 1)
    else:
        print(b[n // 2] - b[n // 2] + 1)

if __name__ == '__main__':
    main()