def main():
    n = int(input())
    i = 1
    while True:
        if n <= i * (i + 1) / 2:
            break
        i += 1
    print(i)

if __name__ == '__main__':
    main()