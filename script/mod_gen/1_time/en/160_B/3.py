def main():
    X = int(input())
    print((X // 500) * 1000 + (X % 500) // 5 * 5)
main()

if __name__ == '__main__':
    main()