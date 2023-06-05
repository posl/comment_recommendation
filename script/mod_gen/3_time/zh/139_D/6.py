def main():
    n = int(input())
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    elif n == 3:
        print(4)
    else:
        print(n * (n - 1) * (n - 2) * (n - 3))

if __name__ == '__main__':
    main()