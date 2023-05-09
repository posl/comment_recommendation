def main():
    x = int(input())
    y = int(input())
    if y < 3:
        print(x - 1)
    elif y < 7:
        print(x)
    else:
        print(x + 1)

if __name__ == '__main__':
    main()