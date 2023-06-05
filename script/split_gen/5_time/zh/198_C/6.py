def main():
    R, X, Y = map(int, input().split())
    if (X ** 2 + Y ** 2) ** (1 / 2) % R == 0:
        print(int((X ** 2 + Y ** 2) ** (1 / 2) / R))
    else:
        print(int((X ** 2 + Y ** 2) ** (1 / 2) // R + 1))
