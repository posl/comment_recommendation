def main():
    x, y = map(float, input().split("."))
    if 0 <= y <= 2:
        print(int(x), end="-")
    elif 3 <= y <= 6:
        print(int(x), end="")
    elif 7 <= y <= 9:
        print(int(x), end="+")
    else:
        print("error")

if __name__ == '__main__':
    main()