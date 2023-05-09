def f(a,b):
    if a==b:
        return a
    elif a%2==0 and b%2==0:
        return f(a//2,b//2)*2
    elif a%2==0 and b%2==1:
        return f(a//2,b//2)*2+1
    elif a%2==1 and b%2==0:
        return f(a//2,b//2)*2+1
    else:
        return f(a//2,b//2)*2+2
a,b=map(int,input().split())
print(f(a,b))

if __name__ == '__main__':
    f()