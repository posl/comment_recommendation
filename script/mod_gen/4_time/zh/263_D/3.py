def main():
    n,l,r = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    s = sum(a[:l])
    for i in range(l,n):
        s += min(a[i],a[l-1])
    print(s)

if __name__ == '__main__':
    main()