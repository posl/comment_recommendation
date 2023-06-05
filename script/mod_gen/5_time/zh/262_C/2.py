def f(x):
    if x==0:
        return 0
    else:
        return x*(x-1)/2
N=int(raw_input())
a=map(int,raw_input().split())
b=[0]*N
for i in range(N):
    b[a[i]-1]=i
ans=0
for i in range(N):
    if i==0:
        if b[i]>b[i+1]:
            ans+=1
    elif i==N-1:
        if b[i]>b[i-1]:
            ans+=1
    else:
        if b[i]>b[i-1] and b[i]>b[i+1]:
            ans+=1
print ans

if __name__ == '__main__':
    f()