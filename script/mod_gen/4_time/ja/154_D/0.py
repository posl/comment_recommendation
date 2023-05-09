def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, sum(p[i:i+K]) / 2 + 0.5 * K)
    print(ans)

if __name__ == '__main__':
    main()