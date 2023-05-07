def main():
    r, c = map(int, input().split())
    if (r % 2 == 0 and c % 2 == 0) or (r % 2 == 1 and c % 2 == 1):
        print("black")
    else:
        print("white")
main()

if __name__ == '__main__':
    main()