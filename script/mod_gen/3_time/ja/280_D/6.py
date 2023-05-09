def main():
    k = int(input())
    n = k
    while True:
        if n % k == 0:
            break
        n += k
    print(n)

if __name__ == '__main__':
    main()