def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = x[1] - x[0]
    for i in range(1, N + 1):
        d = gcd(d, x[i] - x[i - 1])
    print(d)

if __name__ == '__main__':
    main()