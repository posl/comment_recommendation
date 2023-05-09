def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    sum_a = [0]*(n+1)
    for i in range(n):
        sum_a[i+1] = sum_a[i]+a[i]
    ans = 0
    for i in range(n):
        for j in range(i,n):
            if sum_a[j+1]-sum_a[i] == k:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()