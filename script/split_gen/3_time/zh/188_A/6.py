def main():
    x,y = map(int,input().split())
    if x<y:
        if y-x>=3:
            print("No")
        else:
            print("Yes")
    else:
        print("No")
