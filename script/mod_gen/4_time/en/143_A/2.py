def main():
    a, b = map(int, input().split())
    if a - 2*b < 0:
        print(0)
    else:
        print(a - 2*b)

if __name__ == '__main__':
    main()