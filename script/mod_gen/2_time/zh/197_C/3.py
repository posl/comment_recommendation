def main():
    n = int(input())
    a = list(map(int, input().split()))
    min_xor = 2 ** 30
    for i in range(n):
        for j in range(i, n):
            xor = 0
            for k in range(i, j + 1):
                xor ^= a[k]
            min_xor = min(min_xor, xor)
    print(min_xor)

if __name__ == '__main__':
    main()