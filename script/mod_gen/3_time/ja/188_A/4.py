def main():
    x, y = map(int, input().split())
    if abs(x - y) <= 2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()