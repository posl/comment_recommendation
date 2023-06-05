def main():
    n = int(input())
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i)
            if i != n // i:
                print(n // i)
        i += 1

if __name__ == '__main__':
    main()