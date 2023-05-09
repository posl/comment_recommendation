def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = a[0]
    for i in range(1, len(a)):
        m = m * a[i] // gcd(m, a[i])
    print(sum(m - 1 for a in a) % (10**9 + 7))

if __name__ == '__main__':
    main()