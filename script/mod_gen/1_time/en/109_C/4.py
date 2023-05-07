def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    ans = x[1] - x[0]
    for i in range(1, len(x) - 1):
        ans = gcd(ans, x[i + 1] - x[i])
    print(ans)

if __name__ == '__main__':
    main()