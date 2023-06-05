def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    #print(len(a))
    #print(a[0])
    #print(a[len(a)-1])
    #print(a[len(a)-1]-a[0])
    #print(k)
    #print(n)
    if k == 1:
        print(n)
    elif k == n:
        print(1)
    else:
        print(n-k+1)
