def main():
    n, x = map(int, input().split())
    xl = list(map(int, input().split()))
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    ans = abs(x - xl[0])
    for i in range(1, n):
        ans = gcd(ans, abs(x - xl[i]))
    print(ans)

if __name__ == '__main__':
    main()