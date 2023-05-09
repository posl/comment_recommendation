def func(n,x,y):
    if n==1:
        return 0
    elif n==2:
        return x+y
    else:
        return func(n-1,x,y)*2+x+y
n,x,y=map(int,input().split())
print(func(n,x,y))

if __name__ == '__main__':
    func()