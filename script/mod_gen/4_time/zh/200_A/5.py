def main():
    N = int(input())
    if N % 100 == 0:
        century = N // 100
    else:
        century = N // 100 + 1
    print(century)

if __name__ == '__main__':
    main()