def main():
    a,b,c,x=map(int,input().split())
    if x<a:
        print(0)
    elif x<=b:
        print(1)
    else:
        print(1-(b-x)/(b-a))
