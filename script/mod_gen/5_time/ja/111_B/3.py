def main():
    n = int(input())
    n_100 = n // 100
    n_10 = (n % 100) // 10
    n_1 = n % 10
    if n_100 == n_10 and n_10 == n_1:
        print(n)
    else:
        if n_100 == 9:
            print(999)
        else:
            print((n_100 + 1) * 100 + (n_100 + 1) * 10 + (n_100 + 1))

if __name__ == '__main__':
    main()