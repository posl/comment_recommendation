def main():
    r, c = (int(x) for x in input().split())
    if r % 2 == 0:
        if c % 2 == 0:
            print("white")
        else:
            print("black")
    else:
        if c % 2 == 0:
            print("black")
        else:
            print("white")

if __name__ == '__main__':
    main()