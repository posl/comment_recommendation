def main():
    A,B = map(int,input().split())
    if A == 0 and B == 0:
        print(0,0)
    else:
        x = A/(A**2 + B**2)**0.5
        y = B/(A**2 + B**2)**0.5
        print(x,y)
