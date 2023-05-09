def main():
    x, y = map(int, input().split())
    if abs(x-y) >= 3:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()