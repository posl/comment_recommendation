def main():
    import math
    R, X, Y = map(int, input().split())
    distance = math.sqrt(X**2 + Y**2)
    if distance % R == 0:
        print(int(distance / R))
    else:
        print(math.ceil(distance / R))

if __name__ == '__main__':
    main()