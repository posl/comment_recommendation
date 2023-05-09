def main():
    R, X, Y = map(int, input().split())
    D = (X**2 + Y**2)**(1/2)
    if D < R:
        print(2)
    else:
        print(int(D // R) + (0 if D % R == 0 else 1))
