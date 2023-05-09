def main():
    r,c = map(int, input().split())
    if r%2 == 1:
        if c%2 == 1:
            print("black")
        else:
            print("white")
    else:
        if c%2 == 1:
            print("white")
        else:
            print("black")

if __name__ == '__main__':
    main()