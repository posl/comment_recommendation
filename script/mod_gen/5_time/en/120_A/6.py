def main():
    a, b, c = map(int, input().split())
    if a <= b:
        print(c // a)
    else:
        print(b // a)

if __name__ == '__main__':
    main()