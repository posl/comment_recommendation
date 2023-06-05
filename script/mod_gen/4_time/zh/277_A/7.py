def find_x(n,x,p):
    for i in range(n):
        if p[i]==x:
            return i+1
n,x=map(int,input().split())
p=list(map(int,input().split()))
print(find_x(n,x,p))
