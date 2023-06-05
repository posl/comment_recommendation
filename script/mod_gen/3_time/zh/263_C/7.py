def f(n,m):
    if n==1:
        return [[i] for i in range(1,m+1)]
    else:
        return [ [i]+j for i in range(1,m+1) for j in f(n-1,m) if i<j[0] ]
n,m=map(int,input().split())
for i in f(n,m):
    print(*i)

if __name__ == '__main__':
    f()