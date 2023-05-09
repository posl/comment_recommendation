def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(m):
        ans += a[i]
    if ans > n:
        ans = -1
    print(ans)

if __name__ == '__main__':
    main()