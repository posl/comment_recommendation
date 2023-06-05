def main():
    #input
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    #init
    good = [1]*n
    #solve
    for i in range(m):
        if h[a[i]-1] <= h[b[i]-1]:
            good[a[i]-1] = 0
        if h[b[i]-1] <= h[a[i]-1]:
            good[b[i]-1] = 0
    #output
    print(sum(good))

if __name__ == '__main__':
    main()