def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    #print(n,k,q)
    #print(a)
    #print(l)
    #print(l[0])
    #print(a[l[0]-1])
    #print(a[l[0]-1]+1)
    #print(a[l[0]-1]+1<=n)
    #print(a[l[0]-1]+1 not in a)
    #print(a[l[0]-1]+1 not in a)
    #print('----')
    #print(a)
    #print(l)
    #print('----')
    for i in range(q):
        if a[l[i]-1]+1<=n and a[l[i]-1]+1 not in a:
            a[l[i]-1] += 1
    for i in range(k):
        print(a[i],end=' ')

if __name__ == '__main__':
    main()