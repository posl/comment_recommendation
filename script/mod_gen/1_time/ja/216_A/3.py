def main():
    x, y = map(int, input().split("."))
    if 0 <= y <= 2:
        print(x, "-", sep="")
    elif 3 <= y <= 6:
        print(x)
    else:
        print(x, "+", sep="")

if __name__ == '__main__':
    main()