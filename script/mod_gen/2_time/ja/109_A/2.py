def main():
    a, b = map(int, input().split())
    if a % 2 == 1 and b % 2 == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()