def main():
    R,X,Y = map(int,input().split())
    distance = (X**2 + Y**2)**(1/2)
    if distance.is_integer():
        print(int(distance//R))
    else:
        print(int(distance//R + 1))
