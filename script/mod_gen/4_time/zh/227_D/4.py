def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if k == 1:
        print(n)
    else:
        ans = 0
        for i in range(n-k+1):
            if a[i+k-1] - a[i] < ans:
                continue
            else:
                ans = a[i+k-1] - a[i]
        print(ans)

if __name__ == '__main__':
    main()