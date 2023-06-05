def main():
    R, X, Y = map(int, input().split())
    if R*R > X*X + Y*Y:
        print(2)
    else:
        print((X*X + Y*Y + R*R - 1)//(R*R))
