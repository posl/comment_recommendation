def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    for i in range(q):
        if a[l[i]-1] < a[l[i]]:
            a[l[i]-1],a[l[i]] = a[l[i]],a[l[i]-1]
    for i in range(k):
        print(a[i],end=' ')
main()
