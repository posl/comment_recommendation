def main():
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    if x + 3 > y:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()