def main():
    n,k = map(int,input().split())
    ans = 0
    for a in range(1,n+1):
        if a%k == 0:
            ans += n//k
        elif a%k <= k//2:
            ans += n//k
        else:
            ans += n//k + 1
    print(ans**3)

if __name__ == '__main__':
    main()