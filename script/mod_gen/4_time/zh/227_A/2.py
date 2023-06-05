def main():
    n, k, a = map(int, input().split())
    print((k - a) % n)

if __name__ == '__main__':
    main()