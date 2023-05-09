def main():
    W,H,x,y = map(int,input().split())
    print(W*H/2,end=" ")
    if x==W/2 and y==H/2:
        print(1)
    else:
        print(0)
