def main():
    import math
    R, X, Y = map(int, input().split())
    if math.sqrt(X**2 + Y**2) <= R:
        print(2)
        return
    print(math.ceil(math.sqrt(X**2 + Y**2) / R))
