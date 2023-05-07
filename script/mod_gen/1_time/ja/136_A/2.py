def main():
    a, b, c = map(int, input().split())
    if a > b:
        if a - b >= c:
            print(0)
        else:
            print(c - (a - b))
    else:
        print(c)

if __name__ == '__main__':
    main()