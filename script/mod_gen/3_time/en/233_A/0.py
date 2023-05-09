def main():
    x, y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        print(y - x)

if __name__ == '__main__':
    main()