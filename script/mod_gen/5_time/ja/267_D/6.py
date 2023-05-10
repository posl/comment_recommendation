def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n-m+1):
        sum = 0
        for j in range(m):
            sum += (j+1)*a[i+j]
        if sum > ans:
            ans = sum
    print(ans)

if __name__ == '__main__':
    main()