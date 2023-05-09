def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        a = x[i]
        b = x[i+K-1]
        if a >= 0:
            ans = min(ans, b)
        elif b <= 0:
            ans = min(ans, -a)
        else:
            ans = min(ans, min(abs(a)+b, abs(b)+a))
    print(ans)

if __name__ == '__main__':
    main()