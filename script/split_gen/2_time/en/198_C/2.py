def main():
    R, X, Y = map(int, input().split())
    dist = (X**2 + Y**2)**(1/2)
    if dist % R == 0:
        print(int(dist/R))
    else:
        print(int(dist//R)+1)
