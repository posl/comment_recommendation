def main():
    x1,y1,x2,y2=map(int,input().split())
    if abs(x1-x2)%2==0 and abs(y1-y2)%2==0:
        print("Yes")
    elif abs(x1-x2)%2==1 and abs(y1-y2)%2==1:
        print("Yes")
    else:
        print("No")
