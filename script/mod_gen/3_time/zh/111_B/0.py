def main():
    n = int(input())
    while n % 111 != 0:
        n += 1
    print(n)

if __name__ == '__main__':
    main()