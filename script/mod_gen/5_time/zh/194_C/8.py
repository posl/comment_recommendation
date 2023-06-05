def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        ans += (i+1)*(n-i-1)*(a[i]**2)
    print(ans)

if __name__ == '__main__':
    main()