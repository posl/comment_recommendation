def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if i < 10:
            if i % 2 == 1:
                count += 1
        elif i < 100:
            if i % 2 == 1:
                count += 1
        elif i < 1000:
            if i % 2 == 1:
                count += 2
        elif i < 10000:
            if i % 2 == 1:
                count += 2
        elif i < 100000:
            if i % 2 == 1:
                count += 3
    print(count)

if __name__ == '__main__':
    main()