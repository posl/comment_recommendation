def main():
    X, Y = map(int, input().split())
    if X*4 < Y or Y < X*2:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()