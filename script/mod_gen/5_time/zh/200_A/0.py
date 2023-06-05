def main():
    n = int(input())
    century = n // 100
    if n % 100 != 0:
        century += 1
    print(century)

if __name__ == '__main__':
    main()