def main():
    n = int(input())
    x = 1
    while x % n != 0:
        x = x * 2
    print(x)

if __name__ == '__main__':
    main()