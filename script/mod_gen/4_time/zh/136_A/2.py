def main():
    a, b, c = map(int, input().split())
    if a >= b + c:
        print(0)
    else:
        print(c - (a - b))

if __name__ == '__main__':
    main()