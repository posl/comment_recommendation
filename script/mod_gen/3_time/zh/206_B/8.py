def main():
    n = int(input())
    x = 1
    y = 0
    while y < n:
        y += x
        x += 1
    print(x - 1)

if __name__ == '__main__':
    main()