def main():
    # input
    R, X, Y = map(int, input().split())
    # compute
    # output
    if R*R > X*X + Y*Y:
        print(2)
    elif (R*R == X*X + Y*Y) or ((R*R - (X*X + Y*Y)) % (2*R) == 0):
        print((R*R - (X*X + Y*Y)) // (2*R) + 1)
    else:
        print((R*R - (X*X + Y*Y)) // (2*R) + 2)
