def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(m):
        ans += (i+1)*a[n-m+i]
    print(ans)

if __name__ == '__main__':
    main()