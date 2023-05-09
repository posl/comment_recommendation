def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(m)
    ans = 0
    pre = 0
    for i in range(n+1):
        ans += (a[i]-pre-1)//(n+1)
        pre = a[i]
    print(ans)

if __name__ == '__main__':
    main()