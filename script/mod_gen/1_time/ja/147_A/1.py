def main():
    a, b, c = map(int, input().split())
    if a + b + c <= 21:
        print("win")
    else:
        print("bust")

if __name__ == '__main__':
    main()