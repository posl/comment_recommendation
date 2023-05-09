def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    # a.sort(reverse=True)
    ans = -1
    for i in range(n):
        for j in range(i+1,n):
            if (a[i]+a[j])%2 == 0:
                ans = max(ans,a[i]+a[j])
    print(ans)

if __name__ == '__main__':
    main()