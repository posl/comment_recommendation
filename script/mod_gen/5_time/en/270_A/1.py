def main():
    a, b = map(int, input().split())
    if a == b:
        print(a)
    else:
        print(3 - a - b)

if __name__ == '__main__':
    main()