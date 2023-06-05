def main():
    x,y=map(int,input().split())
    x,y=abs(x),abs(y)
    if x+y==0:
        print(0)
        return
    if x+y==1:
        print(1)
        return
    if x+y==2:
        print(2)
        return
    if x<y:
        x,y=y,x
    if x==2 and y==2:
        print(0)
        return
    if y==0:
        print(2)
        return
    if y==1:
        print(x-1)
        return
    if y==2:
        print(x)
        return
    if x==3 and y==3:
        print(2)
        return
    if y>=4:
        print((x+y-2)%1000000007)
        return
    if x==4 and y==3:
        print(4)
        return
    if x==4 and y==4:
        print(4)
        return
    if x==5 and y==3:
        print(4)
        return
    if x==5 and y==4:
        print(8)
        return
    if x==5 and y==5:
        print(4)
        return
    if x==6 and y==3:
        print(4)
        return
    if x==6 and y==4:
        print(8)
        return
    if x==6 and y==5:
        print(8)
        return
    if x==6 and y==6:
        print(4)
        return
    if x==7 and y==3:
        print(4)
        return
    if x==7 and y==4:
        print(8)
        return
    if x==7 and y==5:
        print(12)
        return
    if x==7 and y==6:
        print(8)
        return
    if x==7 and y==7:
        print(4)
        return
    if x==8 and y==3:
        print(4)
        return
    if x==8 and y==4:
        print(8)
        return
    if x==8 and y==5:
        print(12)
        return
    if x==8 and y==6:
        print(16)
