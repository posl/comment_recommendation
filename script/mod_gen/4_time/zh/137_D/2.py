def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[0])
    a = [x[0] for x in ab]
    b = [x[1] for x in ab]
    import bisect
    ans = 0
    for i in range(n):
        if a[i] > m:
            break
        ans += b[i]
        m -= a[i]
    print(ans)

if __name__ == '__main__':
    main()