def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    b = [0]*(m+1)
    for i in range(n):
        b[a[i]] += 1
    k = 0
    for i in range(m+1):
        if b[i] > 0:
            k = i
            break
    if k == 0:
        print(0)
        exit()
    c = [0]*(m+1)
    c[0] = b[0]
    for i in range(1,m+1):
        c[i] = c[i-1]+b[i]
    ans = 0
    for i in range(k,m+1):
        ans += c[i]
    print(ans)

if __name__ == '__main__':
    main()