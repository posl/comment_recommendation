def main():
    n = input()
    print('Yes' if n == n[::-1] else 'No')

if __name__ == '__main__':
    main()