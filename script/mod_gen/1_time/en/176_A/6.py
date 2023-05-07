def takoyaki():
    n,x,t = map(int, input().split())
    if n%x==0:
        print(n//x*t)
    else:
        print(n//x*t+t)

if __name__ == '__main__':
    takoyaki()