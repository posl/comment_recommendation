def f(h,w):
    if h==[]:
        return 1
    else:
        res = 0
        for i in range(1,h[0]+1):
            res += f(h[1:],w[1:])
        return res
h = list(map(int,input().split()))
w = list(map(int,input().split()))
print(f(h,w))
