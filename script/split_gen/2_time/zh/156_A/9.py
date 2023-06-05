def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    #print(n,k)
    #print(a)
    #print(a[n-1],a[n-2],a[n-3],a[n-4],a[n-5],a[n-6])
    if n==2:
        print(a[0]*a[1])
        return
    if a[n-1]>=0:
        if k<=((n*(n-1))/2):
            print(a[n-1]*a[n-2-(k-1)])
        else:
            print(a[0]*a[n-1])
    elif a[n-1]<0:
        if k<=((n*(n-1))/2):
            print(a[0]*a[1+(k-1)])
        else:
            print(a[0]*a[n-1])
