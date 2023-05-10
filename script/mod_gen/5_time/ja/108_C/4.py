def main():
    n,k = map(int,input().split())
    ans = 0
    if k % 2 == 0:
        ans = int(n/k)**3
        if k/2 <= n:
            ans += int((n-k/2)/k+1)**3
    else:
        ans = int(n/k)**3
    print(ans)

if __name__ == '__main__':
    main()