def main():
    import math
    R,X,Y = map(int,input().split())
    distance = math.sqrt(X**2+Y**2)
    if distance%R == 0:
        print(int(distance/R))
    elif distance < R:
        print(2)
    else:
        print(int(distance//R+1))
