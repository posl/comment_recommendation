def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        if a[i] == 0:
            continue
        else:
            b.append(a[i])
    if len(b) < m:
        print(0)
    else:
        b.sort(reverse = True)
        ans = 0
        for i in range(m):
            ans += (i+1)*b[i]
        print(ans)

if __name__ == '__main__':
    main()