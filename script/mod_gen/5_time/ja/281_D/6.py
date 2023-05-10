def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    s = 0
    for i in range(n-k+1):
        if a[i] % d == 0:
            s = max(s,a[i])
    if s == 0:
        print(-1)
    else:
        print(s)

if __name__ == '__main__':
    main()