def main():
    x = input()
    m = int(input())
    n = len(x)
    #print(x,m,n)
    d = 0
    for i in range(n):
        d = max(d,int(x[i]))
    #print(d)
    if d == 1:
        print(n)
        exit()
    l = d
    r = m+1
    while r-l>1:
        mid = (r+l)//2
        #print(mid)
        v = 0
        for i in range(n):
            v = v*mid + int(x[i])
        if v>m:
            r = mid
        else:
            l = mid
    print(l-d)

if __name__ == '__main__':
    main()