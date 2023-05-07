def main():
    n = int(input())
    for i in range(0, n//4 + 1):
        if (n - 4 * i) % 7 == 0:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()