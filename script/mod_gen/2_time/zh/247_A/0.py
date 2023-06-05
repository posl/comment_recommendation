def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    x = 1
    while True:
        if x ** 3 + x ** 2 + x + 1 >= n:
            break
        x += 1
    while True:
        if x ** 3 + x ** 2 + x + 1 >= n and x ** 3 <= n:
            break
        x -= 1
    print(x)

if __name__ == '__main__':
    main()