def swap(x,y):
    return y,x
x,y,z = map(int,input().split())
x,y = swap(x,y)
x,z = swap(x,z)
print(x,y,z)
