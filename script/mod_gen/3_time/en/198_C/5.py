def main():
    R, X, Y = map(int, input().split())
    D = (X ** 2 + Y ** 2) ** 0.5
    if D < R:
        print(2)
        return
    print(int(D // R + (D % R > 0)))
main()
