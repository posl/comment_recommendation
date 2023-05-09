def main():
    row, col = map(int, input().split())
    if row <= 8 and col <= 8:
        print("white")
    else:
        print("black")

if __name__ == '__main__':
    main()