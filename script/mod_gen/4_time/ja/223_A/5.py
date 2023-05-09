def main():
    x = int(input())
    if 0 <= x and x <= 1000 and x % 100 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()