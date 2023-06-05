def f(n):
    if n%2==0:
        return n/2
    else:
        return (n+1)/2
    
N=int(raw_input())
a=map(int,raw_input().split())
b=[]
for i in range(N):
    for j in range(i,N):
        b.append(sorted(a[i:j+1])[f(j-i)])
print sorted(b)[f(N*(N+1)/2)]
