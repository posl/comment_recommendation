def main():
    N = int(input())
    x = 1
    y = 1
    count = 0
    while x * y < N:
        if x < y:
            x += 1
        else:
            y += 1
        count += 1
    print(count)

if __name__ == '__main__':
    main()