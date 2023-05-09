def max(a,b):
    if a>b:
        return a
    else:
        return b
n = int(input())
b = list(map(int,input().split()))
a = [0] * n
a[0] = b[0]
a[n-1] = b[n-2]
for i in range(1,n-1):
    a[i] = max(b[i-1],b[i])
print(sum(a))
