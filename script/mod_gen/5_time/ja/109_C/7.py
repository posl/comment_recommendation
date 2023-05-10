def main():
    N, X = map(int, input().split())
    x = [int(i) for i in input().split()]
    x.append(X)
    x.sort()
    D = []
    for i in range(N):
        D.append(x[i+1] - x[i])
    def gcd(a,b):
        if b == 0:
            return a
        else:
            return gcd(b, a%b)
    ans = D[0]
    for i in range(1, N):
        ans = gcd(ans, D[i])
    print(ans)

if __name__ == '__main__':
    main()