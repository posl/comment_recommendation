def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = [0]*10
    for i in range(10):
        ans[i] = a.count(i)
    print(ans)
    for i in range(1,n):
        tmp = [0]*10
        for j in range(10):
            tmp[(j+a[i])%10] += ans[j]
            tmp[(j*a[i])%10] += ans[j]
        ans = tmp
        print(ans)
    for i in range(10):
        print(ans[i]%998244353)

if __name__ == '__main__':
    main()