def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    print(n,m)
    print(h)
    print(a)
    print(b)
    #print(h[a[0]-1])
    #print(h[b[0]-1])
    #print(h[a[1]-1])
    #print(h[b[1]-1])
    #print(h[a[2]-1])
    #print(h[b[2]-1])
    #print(h[a[0]-1] > h[b[0]-1])
    #print(h[a[1]-1] > h[b[1]-1])
    #print(h[a[2]-1] > h[b[2]-1])
    #print(h[a[0]-1] > h[b[0]-1] and h[a[1]-1] > h[b[1]-1] and h[a[2]-1] > h[b[2]-1])
    #print(h[0] > h[1])
    count = 0
    for i in range(m):
        if h[a[i]-1] > h[b[i]-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()