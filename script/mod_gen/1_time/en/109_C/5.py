def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    d = abs(X - x[0])
    for i in range(1, N):
        d = gcd(d, abs(X - x[i]))
    print(d)

if __name__ == '__main__':
    main()