def isTriangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False
N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if isTriangle(L[i],L[j],L[k]):
                ans += 1
print(ans)
