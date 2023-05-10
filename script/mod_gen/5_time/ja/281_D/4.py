def main():
    n,k,d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k == 1:
        if a[0] % d == 0:
            print(a[0])
        else:
            print(-1)
        return
    if n < k:
        print(-1)
        return
    if a[0] % d == 0:
        print(a[0] + d * (k-1))
        return
    for i in range(n-k+1):
        if a[i] % d == 0:
            print(a[i] + d * (k-1))
            return
    print(-1)
    return

if __name__ == '__main__':
    main()