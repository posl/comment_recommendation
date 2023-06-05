def solve(n,k,a):
    if k==1:
        return "Yes"
    for i in range(0,k):
        if a[i]>a[i+k]:
            return "No"
    return "Yes"
n,k=map(int,input().split())
a=list(map(int,input().split()))
print(solve(n,k,a))
