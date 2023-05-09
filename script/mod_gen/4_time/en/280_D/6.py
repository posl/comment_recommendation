def main():
    k = int(input())
    n = 1
    while True:
        if n % k == 0:
            break
        n += 1
    print(n)

if __name__ == '__main__':
    main()