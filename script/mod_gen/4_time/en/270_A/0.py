def main():
    a, b = map(int, input().split())
    if a == 0:
        print(b)
    elif b == 0:
        print(a)
    else:
        print(3 - a - b)

if __name__ == '__main__':
    main()