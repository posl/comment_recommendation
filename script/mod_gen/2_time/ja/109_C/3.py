def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    d = abs(x[0] - X)
    for i in range(1, N):
        d = gcd(d, abs(x[i] - X))
    print(d)

if __name__ == '__main__':
    main()