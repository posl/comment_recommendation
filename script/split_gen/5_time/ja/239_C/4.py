def main():
    x1,y1,x2,y2 = map(int,input().split())
    if x1 == x2 and y1 == y2:
        print("No")
    elif x1 == x2:
        print("Yes")
    elif y1 == y2:
        print("Yes")
    elif abs(x1-x2) == abs(y1-y2):
        print("Yes")
    else:
        print("No")
