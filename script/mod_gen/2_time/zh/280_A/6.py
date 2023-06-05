def main():
    a,b = map(int,input().split())
    l = 0
    r = 10**18
    while r - l > 1e-6:
        mid = (l+r)/2
        if mid + a/(mid**0.5) < b:
            l = mid
        else:
            r = mid
    print(l)

if __name__ == '__main__':
    main()