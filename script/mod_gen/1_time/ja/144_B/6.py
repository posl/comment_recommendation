def main():
    n = int(input())
    if n == 1:
        print('No')
        return
    for i in range(1, 10):
        if n % i == 0 and n // i < 10:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()