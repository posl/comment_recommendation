def main():
    R, X, Y = map(int, input().split())
    if (X**2 + Y**2) < R**2:
        print(2)
    else:
        print((X**2 + Y**2)**(1/2) // R + 1)
