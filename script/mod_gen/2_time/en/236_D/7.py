def f(a):
    if len(a) == 1:
        return a[0]
    else:
        return max([a[0]^a[i] + f(a[1:i]+a[i+1:]) for i in range(1,len(a))])
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
print(f([a[i][j] for i in range(n) for j in range(i+1,n)]))
