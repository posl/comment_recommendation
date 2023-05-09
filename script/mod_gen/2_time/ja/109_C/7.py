def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    # x[i]とx[i+1]の差の最大公約数を求める
    diff = [x[i+1]-x[i] for i in range(N)]
    g = diff[0]
    for i in range(1, N):
        g = gcd(g, diff[i])
    print(g)

if __name__ == '__main__':
    main()