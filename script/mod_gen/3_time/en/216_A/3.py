def main():
    x, y = map(int, input().split("."))
    if y <= 2:
        print(str(x) + "-")
    elif y <= 6:
        print(x)
    elif y <= 9:
        print(str(x) + "+")

if __name__ == '__main__':
    main()