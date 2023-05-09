def main():
    R, C = map(int,input().split())
    black = [2, 4, 6, 8, 10, 12, 14]
    white = [1, 3, 5, 7, 9, 11, 13]
    if R in black:
        if C in black:
            print("black")
        else:
            print("white")
    else:
        if C in black:
            print("white")
        else:
            print("black")

if __name__ == '__main__':
    main()