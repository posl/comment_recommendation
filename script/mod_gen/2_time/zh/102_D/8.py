def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    s = sum(a)
    ans = s
    p = 0
    q = 0
    for i in range(1,n):
        p += a[i-1]
        q += a[i-1]
        r = s-p
        s = r
        ans = min(ans,abs(max(p,q,r,s)-min(p,q,r,s)))
    print(ans)

if __name__ == '__main__':
    main()