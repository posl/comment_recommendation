def f(n,k,h):
    h.sort()
    return h[k-1]-h[0]
n,k=map(int,input().split())
h=[int(input()) for i in range(n)]
print(f(n,k,h))
