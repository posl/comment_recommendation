def main():
    R, X, Y = map(int, input().split())
    D = ((X ** 2) + (Y ** 2)) ** (1 / 2)
    if D == R:
        print(1)
    elif D <= 2 * R:
        print(2)
    else:
        if D % R == 0:
            print(int(D / R))
        else:
            print(int(D / R) + 1)
