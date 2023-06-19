def main():
    x, y = map(int, input().split())
    if x < y and x + 3 > y:
        print("Yes")
    elif x > y and x < y + 3:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()