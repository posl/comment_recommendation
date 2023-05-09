def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N+1):
        if a%K == 0:
            ans += (N//K)**3
        elif a%K == K//2:
            ans += (N//K+1)**3
    print(ans)

if __name__ == '__main__':
    main()