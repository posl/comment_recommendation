def main():
    # input
    R, X, Y = map(int, input().split())
    # compute
    # output
    print( (X**2+Y**2)**(1/2)//R if (X**2+Y**2)**(1/2)%R == 0 else (X**2+Y**2)**(1/2)//R+1 )
