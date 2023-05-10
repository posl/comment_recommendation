def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = []
    for i in range(N):
        d.append(x[i+1] - x[i])
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    ans = d[0]
    for i in range(1, N):
        ans = gcd(ans, d[i])
    print(ans)

if __name__ == '__main__':
    main()