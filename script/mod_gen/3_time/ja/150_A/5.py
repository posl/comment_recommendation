def main():
    k, x = map(int, input().split())
    print('Yes' if x <= 500 * k else 'No')

if __name__ == '__main__':
    main()