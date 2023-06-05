def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if i < 10:
            count += 1
        elif i < 100:
            count += 1
        elif i < 1000:
            count += 1
        elif i < 10000:
            count += 1
        elif i < 100000:
            count += 1
        elif i < 1000000:
            count += 1
        elif i < 10000000:
            count += 1
        elif i < 100000000:
            count += 1
        elif i < 1000000000:
            count += 1
        elif i < 10000000000:
            count += 1
        elif i < 100000000000:
            count += 1
        elif i < 1000000000000:
            count += 1
        elif i < 10000000000000:
            count += 1
        elif i < 100000000000000:
            count += 1
        elif i < 1000000000000000:
            count += 1
        elif i < 10000000000000000:
            count += 1
        elif i < 100000000000000000:
            count += 1
        elif i < 1000000000000000000:
            count += 1
        elif i < 10000000000000000000:
            count += 1
    print(count)

if __name__ == '__main__':
    main()