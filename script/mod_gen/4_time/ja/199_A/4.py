def main():
    A, B, C = map(int, input().split())
    print('Yes' if A**2 + B**2 < C**2 else 'No')

if __name__ == '__main__':
    main()