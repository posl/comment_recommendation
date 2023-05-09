def main():
    n = int(input())
    x = 1
    y = 1
    for i in range(1, n):
        x += 1
        y += 1
        if x * y > n:
            break
    print(x + y - 2)

if __name__ == '__main__':
    main()