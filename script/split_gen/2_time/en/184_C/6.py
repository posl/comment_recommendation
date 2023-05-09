def main():
    r1,c1 = map(int,input().split())
    r2,c2 = map(int,input().split())
    if r1==r2 and c1==c2:
        print(0)
    elif r1+c1==r2+c2 or r1-c1==r2-c2 or abs(r1-r2)+abs(c1-c2)<=3:
        print(1)
    elif (r1+c1-r2-c2)%2==0 or abs(r1-r2)+abs(c1-c2)<=6 or abs((r1+c1)-(r2+c2))<=3 or abs((r1-c1)-(r2-c2))<=3:
        print(2)
    else:
        print(3)
main()
I have a problem with the function abs() in python. I have a list of coordinates and I want to sort them by the distance from a point. I tried to use the function abs() but it did not work. Here is the code:
