def main():
    A, B = map(int, input().split())
    print(100 * (1 - (B / A)))

if __name__ == '__main__':
    main()