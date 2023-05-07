def main():
    n,k = map(int, input().split())
    ans = 0
    if k % 2 == 0:
        ans = pow(n//k,3)
        if n % k >= k//2:
            ans += pow(n//k+1,3)
    else:
        ans = pow(n//k,3)
    print(ans)

if __name__ == '__main__':
    main()