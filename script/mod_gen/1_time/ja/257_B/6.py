def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    for i in range(q):
        if l[i] == 1:
            a[l[i]-1],a[l[i]] = a[l[i]],a[l[i]-1]
        elif l[i] == k:
            a[l[i]-2],a[l[i]-1] = a[l[i]-1],a[l[i]-2]
        else:
            if a[l[i]-2] > a[l[i]]:
                a[l[i]-2],a[l[i]-1] = a[l[i]-1],a[l[i]-2]
            elif a[l[i]] > a[l[i]-1]:
                a[l[i]-1],a[l[i]] = a[l[i]],a[l[i]-1]
    for i in range(k):
        print(a[i],end=' ')

if __name__ == '__main__':
    main()