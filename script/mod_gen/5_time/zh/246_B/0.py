def main():
    A, B = map(int, input().split())
    print(A / (A ** 2 + B ** 2) ** 0.5, B / (A ** 2 + B ** 2) ** 0.5)

if __name__ == '__main__':
    main()