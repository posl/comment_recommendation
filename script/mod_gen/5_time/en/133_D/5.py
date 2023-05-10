def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    for i in range(1, n):
        x ^= a[i]
    x ^= a[0]
    print(*[x^a[i] for i in range(n)])

if __name__ == '__main__':
    main()