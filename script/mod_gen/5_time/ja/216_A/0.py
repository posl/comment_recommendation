def main():
    x, y = map(int, input().split("."))
    if 0 <= y <= 2:
        print(str(x)+"-")
    elif 3 <= y <= 6:
        print(str(x))
    elif 7 <= y <= 9:
        print(str(x)+"+")

if __name__ == '__main__':
    main()