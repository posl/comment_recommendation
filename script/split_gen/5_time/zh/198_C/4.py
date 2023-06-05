def main():
    R, X, Y = map(int, input().split())
    if X*X+Y*Y < R*R:
        print(2)
    else:
        print((X*X+Y*Y+R*R-1)//(R*R))
