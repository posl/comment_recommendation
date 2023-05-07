def main():
    a, b = map(int, input().split())
    if b * 2 > a:
        print(0)
    else:
        print(a - b * 2)

if __name__ == '__main__':
    main()