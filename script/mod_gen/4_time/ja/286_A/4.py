def main():
    n,p,q,r,s = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        if (i+1) >= p and (i+1) <= q:
            b.append(a[i+(s-r)])
        elif (i+1) >= r and (i+1) <= s:
            b.append(a[i-(s-r)])
        else:
            b.append(a[i])
    print(*b)

if __name__ == '__main__':
    main()