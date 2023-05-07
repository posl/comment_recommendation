def main():
    x, y = input().split(".")
    y = int(y)
    if y <= 2:
        print(x + "-")
    elif y <= 6:
        print(x)
    else:
        print(x + "+")

if __name__ == '__main__':
    main()