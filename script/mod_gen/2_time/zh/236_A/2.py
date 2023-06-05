def main():
    #a, n = map(int, input().split(" "))
    a, n = 2, 767090
    count = 0
    while n > 1:
        if n % a == 0:
            n = n / a
            count += 1
        else:
            n = n - 1
            count += 1
    print(count)

if __name__ == '__main__':
    main()