def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a = sorted(a)
    for i in range(n-k):
        if a[i] >= a[i+k]:
            print("No")
            return
    print("Yes")
