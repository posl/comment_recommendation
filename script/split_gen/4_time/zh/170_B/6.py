def main():
    x,y = map(int,input().split())
    if y%2==0:
        if 2*x<=y and y<=4*x:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
