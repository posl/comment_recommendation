def main():
    k = int(input())
    n = 1
    while True:
        if k%n == 0:
            k = k//n
            n = 1
        if k == 1:
            break
        n += 1
    print(n)
main()

if __name__ == '__main__':
    main()