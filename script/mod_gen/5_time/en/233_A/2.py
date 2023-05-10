def main():
    x, y = map(int, input().split())
    if y % 10 == 0:
        print(int(y/10) - int(x/10))
    else:
        print(int(y/10) - int(x/10) + 1)

if __name__ == '__main__':
    main()