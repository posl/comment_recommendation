def main():
    r,x,y = map(int,input().split())
    if x**2 + y**2 < r**2:
        print(2)
    else:
        print(int((x**2 + y**2)**(1/2)//r) + 1)
