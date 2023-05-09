def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.append(m)
    b = [0]*(n+1)
    for i in range(n):
        b[i] = a[i+1] - a[i] - 1
    b[n] = a[0] + m - a[n] - 1
    if m == 1:
        print(0)
        exit()
    if n == 1:
        if a[0] == 0 and a[1] == 1:
            print(0)
        else:
            print(1)
        exit()
    k = min(b)
    ans = 0
    for i in range(n+1):
        ans += (b[i] + k - 1)//k
    print(ans)

if __name__ == '__main__':
    main()