def main():
    a, b, c, d = map(int, input().split())
    if (c + d - 1) // d >= (a + b - 1) // b:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()