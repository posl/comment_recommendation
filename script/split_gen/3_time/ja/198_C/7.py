def main():
    import math
    R, X, Y = map(int, input().split())
    if X == 0 and Y == 0:
        print(0)
        return
    if X == Y:
        print(int(math.sqrt(X**2 + Y**2) / R) + 1)
        return
    if X == 0:
        print(int(Y / R) + 1)
        return
    if Y == 0:
        print(int(X / R) + 1)
        return
    print(int(math.sqrt(X**2 + Y**2) / R) + 1)
