def main():
    x, y = map(int, input().split())
    if y - x < 3:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()