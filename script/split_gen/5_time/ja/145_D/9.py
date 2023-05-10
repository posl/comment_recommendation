def main():
    X,Y = map(int, input().split())
    print(0 if (X+Y)%3 != 0 or X*2 < Y or Y*2 < X else 151840682)
