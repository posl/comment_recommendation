def main():
    R, C = map(int, input().split())
    if R % 2 == 0:
        if C % 2 == 0:
            print("white")
        else:
            print("black")
    else:
        if C % 2 == 0:
            print("black")
        else:
            print("white")

if __name__ == '__main__':
    main()