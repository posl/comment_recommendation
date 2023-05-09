def main():
    n = int(input())
    if n <= 9:
        print('No')
    else:
        for i in range(1, 10):
            if n % i == 0 and 1 <= n // i <= 9:
                print('Yes')
                break
        else:
            print('No')

if __name__ == '__main__':
    main()