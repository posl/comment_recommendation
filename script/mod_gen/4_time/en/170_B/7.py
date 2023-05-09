def main():
    x,y = map(int,input().split())
    if (y % 2 == 0) and (2 * x <= y) and (4 * x >= y):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()