def main():
    x, y = map(int, input().split())
    if y % 2 == 0 and x <= y//2 <= x*2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()