def main():
    N, K = map(int, input().split())
    h = [int(input()) for i in range(N)]
    h.sort()
    ans = 10000000000000
    for i in range(N-K+1):
        ans = min(ans, h[i+K-1]-h[i])
    print(ans)
main()

if __name__ == '__main__':
    main()