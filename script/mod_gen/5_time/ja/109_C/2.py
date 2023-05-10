def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = []
    for i in range(N):
        d.append(x[i+1] - x[i])
    import math
    ans = d[0]
    for i in range(1, N):
        ans = math.gcd(ans, d[i])
    print(ans)

if __name__ == '__main__':
    main()