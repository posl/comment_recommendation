def main():
    x, y = map(int, input().split())
    if x * 4 < y or y < x * 2:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()