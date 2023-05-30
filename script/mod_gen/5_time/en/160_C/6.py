def solve(k,n,a):
    distance = []
    for i in range(n):
        if i == n-1:
            distance.append(k-a[i]+a[0])
        else:
            distance.append(a[i+1]-a[i])
    distance.sort()
    distance.pop()
    return sum(distance)
k,n = map(int,input().split())
a = list(map(int,input().split()))
print(solve(k,n,a))
