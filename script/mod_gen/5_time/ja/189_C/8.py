def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        for j in range(i,n):
            tmp = min(a[i:j+1])
            ans = max(ans, tmp*(j-i+1))
    print(ans)

if __name__ == '__main__':
    main()