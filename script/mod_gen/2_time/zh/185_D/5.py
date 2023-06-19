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
    if a[0] != 1:
        a.insert(0,0)
    if a[-1] != n:
        a.append(n+1)
    print(a)
    ans = 0
    for i in range(1,len(a)):
        if a[i] - a[i-1] - 1 > 0:
            ans += (a[i] - a[i-1] - 1) // m
            if (a[i] - a[i-1] - 1) % m != 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()