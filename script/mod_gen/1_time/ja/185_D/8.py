def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(n+1)
    a.insert(0,0)
    if m == 0:
        print(1)
        exit()
    if m == n:
        print(0)
        exit()
    l = []
    for i in range(m+1):
        l.append(a[i+1]-a[i]-1)
    k = min(l)
    ans = 0
    for i in l:
        ans += i//k
        if i%k != 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()