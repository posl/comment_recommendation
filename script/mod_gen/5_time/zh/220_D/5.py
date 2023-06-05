def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = [0]*10
    for i in range(10):
        ans[i] = 0
    ans[a[-1]] = 1
    for i in range(n-1):
        tmp = [0]*10
        for j in range(10):
            tmp[(j+a[n-2-i])%10] += ans[j]
            tmp[(j*a[n-2-i])%10] += ans[j]
        ans = tmp
    for i in range(10):
        print(ans[i]%998244353)

if __name__ == '__main__':
    main()