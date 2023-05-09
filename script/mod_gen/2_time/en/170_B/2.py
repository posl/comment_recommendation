def main():
    X, Y = map(int, input().split())
    if X * 4 >= Y and X * 2 <= Y:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()