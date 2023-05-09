def main():
    x = int(input())
    y = 100
    n = 0
    while y < x:
        y = int(y * 1.01)
        n += 1
    print(n)

if __name__ == '__main__':
    main()