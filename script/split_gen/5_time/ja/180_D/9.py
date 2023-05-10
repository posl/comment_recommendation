def train(x,y,a,b):
    exp=0
    while True:
        if x*a>=y:
            break
        else:
            exp+=1
            x*=a
    exp+=(y-x)//b
    if (y-x)%b!=0:
        exp+=1
    return exp
x,y,a,b=map(int,input().split())
print(train(x,y,a,b))
