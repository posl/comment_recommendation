def main():
    R, C = map(int, input().split())
    if (R + C) % 2 == 0:
        print("black")
    else:
        print("white")
main()

if __name__ == '__main__':
    main()