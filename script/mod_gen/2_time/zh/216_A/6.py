def main():
    x, y = input().split(".")
    y = int(y)
    x = int(x)
    if 0 <= y <= 2:
        print(str(x) + "-")
    elif 3 <= y <= 6:
        print(str(x))
    else:
        print(str(x) + "+")

if __name__ == '__main__':
    main()