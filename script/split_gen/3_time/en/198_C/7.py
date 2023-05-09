def main():
    R, X, Y = map(int, input().split())
    if X == 0 and Y == 0:
        print(0)
    else:
        dist = (X ** 2 + Y ** 2) ** 0.5
        if dist % R == 0:
            print(int(dist / R))
        else:
            print(int(dist // R) + 1)
