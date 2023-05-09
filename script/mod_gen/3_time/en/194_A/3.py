def main():
    a, b = map(int, input().split())
    if 15 <= a + b and 8 <= b:
        print(1)
    elif 10 <= a + b and 3 <= b:
        print(2)
    elif 3 <= a + b:
        print(3)
    else:
        print(4)

if __name__ == '__main__':
    main()