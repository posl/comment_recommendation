def main():
    r,c = map(int,input().split())
    if r > 0 and r <= 15 and c > 0 and c <= 15:
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