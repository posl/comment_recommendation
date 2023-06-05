def get_num(n,x,y):
    if n == 1:
        return 0
    if n == 2:
        return x + y
    else:
        return get_num(n-1,x,y) + get_num(n-2,x,y) + x
N,X,Y = map(int,input().split())
print(get_num(N,X,Y))
