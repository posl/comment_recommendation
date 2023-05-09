def main():
    r,c = map(int,input().split())
    if 1 <= r and r <= 15 and 1 <= c and c <= 15:
        if r % 2 == 0 and c % 2 == 0:
            print("white")
        elif r % 2 == 0 and c % 2 == 1:
            print("black")
        elif r % 2 == 1 and c % 2 == 0:
            print("black")
        elif r % 2 == 1 and c % 2 == 1:
            print("white")

if __name__ == '__main__':
    main()