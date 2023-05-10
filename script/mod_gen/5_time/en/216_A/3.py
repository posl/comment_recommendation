def main():
    x, y = map(int, input().split("."))
    if y <= 2:
        print("{}-".format(x))
    elif y <= 6:
        print(x)
    else:
        print("{}+".format(x))

if __name__ == '__main__':
    main()