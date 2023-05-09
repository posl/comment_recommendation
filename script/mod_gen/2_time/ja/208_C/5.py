def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = [0]*n
    for i in range(n):
        if k >= n-i:
            ans[i] += k//(n-i)
            k %= (n-i)
        else:
            ans[i] += k
            break
    for i in range(n):
        print(ans[i]+a[i]//a[0])

if __name__ == '__main__':
    main()