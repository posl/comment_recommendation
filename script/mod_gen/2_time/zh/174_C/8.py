def main():
    n, d = map(int, input().split())
    count = 0
    for i in range(n):
        x, y = map(int, input().split())
        if (x ** 2 + y ** 2) ** 0.5 <= d:
            count += 1
    print(count)

if __name__ == '__main__':
    main()