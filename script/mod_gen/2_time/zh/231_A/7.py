def main():
    n,d = map(int,input().split())
    l = []
    r = []
    for i in range(n):
        a,b = map(int,input().split())
        l.append(a)
        r.append(b)
    l.sort()
    r.sort()
    ans = 0
    i = 0
    j = 0
    while i < n:
        if l[i] <= r[j]:
            ans += 1
            i += 1
        else:
            ans -= 1
            j += 1
    print(ans)

if __name__ == '__main__':
    main()