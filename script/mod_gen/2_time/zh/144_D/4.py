def main():
    n = int(input())
    count = 0
    while n != 2:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
        count += 1
    print(count + 2)

if __name__ == '__main__':
    main()