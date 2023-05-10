def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    total = 0
    for i in range(n-1):
        for j in range(i+1, n):
            total += a[i] * a[j]
            total %= mod
    print(total)

if __name__ == '__main__':
    main()