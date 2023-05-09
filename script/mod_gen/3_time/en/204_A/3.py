def main():
    x, y = [int(i) for i in input().split()]
    if x == y:
        print(x)
    else:
        print(3 - x - y)

if __name__ == '__main__':
    main()