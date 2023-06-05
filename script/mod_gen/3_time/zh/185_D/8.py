def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if m == 0:
        print(1)
        return
    if n == m:
        print(0)
        return
    if n > m:
        print(1)
        return
    b = []
    for i in range(m-1):
        b.append(a[i+1]-a[i]-1)
    b.sort()
    ans = 0
    for i in range(m-n):
        ans += b[i]
    print(ans+1)
    return

if __name__ == '__main__':
    main()