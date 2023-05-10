def main():
    x = int(input())
    n = 100
    count = 0
    while n < x:
        n = n + n // 100
        count = count + 1
    print(count)

if __name__ == '__main__':
    main()