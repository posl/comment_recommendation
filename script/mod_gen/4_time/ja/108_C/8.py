def main():
    N,K = map(int,input().split())
    ans = 0
    if K%2 == 0:
        ans += (N//K)**3
        if (N+K//2)%K < K:
            ans += (N+K//2)//K
        print(ans)
    else:
        print((N//K)**3)

if __name__ == '__main__':
    main()