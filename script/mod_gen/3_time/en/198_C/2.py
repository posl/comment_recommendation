def main():
    R, X, Y = map(int, input().split())
    d = ((X ** 2) + (Y ** 2)) ** 0.5
    if d % R == 0:
        print(int(d / R))
    else:
        print(int(d / R) + 1)

if __name__ == '__main__':
    main()