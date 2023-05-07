def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = []
    for i in range(N):
        d.append(x[i+1]-x[i])
    gcd = d[0]
    for i in range(1, N):
        gcd = gcd2(gcd, d[i])
    print(gcd)

if __name__ == '__main__':
    main()