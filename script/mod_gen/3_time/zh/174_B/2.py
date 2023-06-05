def main():
    n, d = map(int, input().split())
    count = 0
    for i in range(n):
        x, y = map(int, input().split())
        if d >= (x ** 2 + y ** 2) ** (1 / 2):
            count += 1
    print(count)

if __name__ == '__main__':
    main()